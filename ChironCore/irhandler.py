from ast import expr
import antlr4
import pickle

from turtparse.parseError import *
from turtparse.tlangParser import tlangParser
from turtparse.tlangLexer import tlangLexer

from ChironAST import ChironAST


def getParseTree(progfl):
    input_stream = antlr4.FileStream(progfl)
    print(input_stream)
    try:
        lexer = tlangLexer(input_stream)
        stream = antlr4.CommonTokenStream(lexer)
        lexer._listeners = [SyntaxErrorListener()]
        tparser = tlangParser(stream)
        tparser._listeners = [SyntaxErrorListener()]
        tree = tparser.start()
    except Exception as e:
        print("\033[91m\n====================")
        print(e.__str__() + "\033[0m\n")
        exit(1)

    return tree


class IRHandler:
    def __init__(self, ir=None, cfg=None):
        # statement list
        self.ir = ir
        # control flow graph
        self.cfg = cfg
        self.sym_tab = {"_globals": {"offsets": {}}}
        self.fpc = -1

    def setIR(self, ir):
        self.ir = ir

    def setCFG(self, cfg):
        self.cfg = cfg

    def dumpIR(self, filename, ir):
        with open(filename, "wb") as f:
            pickle.dump(ir, f)

    def loadIR(self, filename):
        f = open(filename, "rb")
        ir = pickle.load(f)
        self.ir = ir
        return ir

    def updateJump(self, stmtList, index, pos):
        stmt, tgt = stmtList[index]
        # Don't update the conditional nodes whose
        # loops and targets are above the insertion point
        # since these don't get affected in any way.
        if tgt > 0 and index + tgt > pos:
            newTgt = tgt + 1
            # update curr conditional instruction's target
            stmtList[index] = (stmt, newTgt)
            # update the target instruction's jump value
            # if it is a backedge, else leave it as is.
            backJumpInstr, backJmpTgt = stmtList[index + tgt - 1]
            if backJmpTgt < 0:
                print(f"Loop Target : {backJumpInstr}, {backJmpTgt}")
                stmtList[index + tgt - 1] = (backJumpInstr, backJmpTgt - 1)

    def addInstruction(self, stmtList, inst, pos):
        """[summary]

        Args:
            stmtList ([List]): List of IR Statments
            inst ([ChironAST.Instruction type]): Instruction to be added. Should be of type Instruction(AST).
            pos ([int]): Position in IR List to add the instruction.
        """
        if pos >= len(stmtList):
            print("[error] POSITION given is past the instruction list.")
            return

        if isinstance(inst, ChironAST.ConditionCommand):
            print("[Skip] Instruction Type not supported for addition. \n")
            return
        index = 0

        # We must consider the conditional jumps and targets of
        # instructions that appear before the position where the
        # instruction must be added. Other conditional statements
        # will just shift without change of labels since
        # all the jump target numbers are relative.
        while index < pos:
            if isinstance(stmtList[index][0], ChironAST.ConditionCommand):
                # Update the target of this conditional statement and the
                # target statment's target number accordingly.
                updateJump(stmtList, index, pos)
            index += 1
        # We only allow non-jump statement addition as of now.
        stmtList.insert(pos, (inst, 1))

    def removeInstruction(self, stmtList, pos):
        """[summary]

        Replace by a no-op as of now. (Sumit: Kinda works)

        Args:
            stmtList ([List]): List of IR Statments
            pos ([int]): Position in IR List to remove the instruction.
        """
        if pos >= len(stmtList):
            print("[error] POSITION given is past the instruction list.")
            return

        inst = stmtList[pos][0]
        if isinstance(inst, ChironAST.ConditionCommand):
            print("[Skip] Instruction Type not supported for removal. \n")
            return

        if "__rep_counter_" in str(stmtList[pos][0]):
            print("[Skip] Instruction affecting loop counter. \n")
            return

        # We only allow non-jump/non-conditional statement removal as of now.
        stmtList[pos] = (ChironAST.NoOpCommand(), 1)

    def pretty_print(self, irList):
        """
            We pass a IR list and print it here.
        """
        print("\n========== Chiron IR ==========\n")
        print("The first label before the opcode name represents the IR index or label \non the control flow graph for that node.\n")
        print("The number after the opcode name represents the jump offset \nrelative to that statement.\n")

        for idx, item in enumerate(irList):
            if isinstance(item[0], ChironAST.ProcedureDeclaration):
                params = item[0].params.__str__()[1:-1]
                # params = params.replace(":", "")
                params = params.replace("'", "")
                print(f"[L{idx}]".rjust(5), f"func @{item[0].name}({params}):")
            elif not (isinstance(item[0], ChironAST.ConditionCommand)):
                if idx < self.fpc:
                    print(f"[L{idx}]".rjust(5), f"\t{item[0]}")
                else:
                    print(f"[L{idx}]".rjust(5), f"{item[0]}")
            else:
                if idx < self.fpc:
                    print(f"[L{idx}]".rjust(5), f"\t{item[0]} [{item[1]}]")
                else:
                    print(f"[L{idx}]".rjust(5), f"{item[0]} [{item[1]}]")

    def flattenIR(self, irList):
        flatList = []
        # print(irList)

        irList.sort(key=lambda x: isinstance(x[0], ChironAST.ProcedureDeclaration), reverse=True)
        pc = 0

        for (item, ntgt) in irList:
            if isinstance(item, ChironAST.ProcedureDeclaration):
                # print(f"Flattening procedure: {item.name} with params {item.params}")
                # print(f"Procedure body: {item.body}")
                head_idx = len(flatList)
                flatList.append((item, -1))
                pc += 1

                for stmt, tgt in item.body:
                    if(isinstance(stmt, ChironAST.ProcedureDeclaration)):
                        raise SyntaxError(f"Nested procedure declaration found: {stmt.name}. This is not supported.")

                    flatList.append((stmt, pc + tgt))
                    pc += 1

                # print(ntgt, pc, head_idx)
                flatList[head_idx] = (item, ntgt + len(flatList) - 1)
            elif isinstance(item, ChironAST.AssignmentCommand):
                lhs_name = item.lvar.varname.replace(":", "")
                if self.sym_tab["_globals"]["offsets"].get(lhs_name) is None:
                    self.sym_tab["_globals"]["offsets"][lhs_name] = len(self.sym_tab["_globals"]["offsets"])
                flatList.append((item, pc + ntgt))
                pc += 1
            else:
                flatList.append((item, pc + ntgt))
                pc += 1

        # print("\n========== Flattened IR ==========\n")
        # for idx, item in enumerate(flatList):
        #     print(f"[L{idx}]".rjust(5), item[0], f"[{item[1]}]")
        return flatList

    def flatToTAC(self, flatList):
        three_ac_list = []
        # Maps: original_flatlist_index -> index_in_3ac_list
        pc_map = {}
        temp_counter = 0

        def get_next_temp():
            nonlocal temp_counter
            name = f"__t{temp_counter}"
            temp_counter += 1
            return name

        def reduce_expression(expr):
            instrs = []

            if isinstance(expr, (ChironAST.Num, ChironAST.Var, ChironAST.BoolTrue, ChironAST.BoolFalse)):
                return expr, []

            if isinstance(expr, ChironAST.ProcedureCallExpr):
                reduced_args = []
                for arg in expr.args:
                    arg_var, arg_steps = reduce_expression(arg)
                    instrs.extend(arg_steps)
                    reduced_args.append(arg_var)

                # Push parameters in order
                for r_arg in reduced_args:
                    instrs.append(ChironAST.ParamCommand(r_arg))

                temp_result = get_next_temp()
                instrs.append(ChironAST.CallN(expr.name, len(reduced_args)))
                instrs.append(ChironAST.StackDealloc(len(reduced_args)))
                instrs.append(ChironAST.AssignmentCommand(
                    ChironAST.Var(temp_result), 
                    ChironAST.RetVal() 
                ))
                return ChironAST.Var(temp_result), instrs

            if isinstance(expr, (ChironAST.BinArithOp, ChironAST.BinCondOp, ChironAST.AND, ChironAST.OR)):
                left_op, left_instrs = reduce_expression(expr.lexpr)
                right_op, right_instrs = reduce_expression(expr.rexpr)

                instrs.extend(left_instrs)
                instrs.extend(right_instrs)

                temp = get_next_temp()
                # Create a simplified version of the node with leaf operands
                new_op_node = type(expr)(left_op, right_op)
                instrs.append(ChironAST.AssignmentCommand(ChironAST.Var(temp), new_op_node))

                return ChironAST.Var(temp), instrs

            # 4. UNARY OPERATIONS (NOT, UMinus)
            if isinstance(expr, (ChironAST.UnaryArithOp, ChironAST.NOT)):
                operand, op_instrs = reduce_expression(expr.expr)
                instrs.extend(op_instrs)

                temp = get_next_temp()
                new_op_node = type(expr)(operand)
                instrs.append(ChironAST.AssignmentCommand(ChironAST.Var(temp), new_op_node))

                return ChironAST.Var(temp), instrs

            # TODO: flatten condition as well

            raise SyntaxError(f"Unsupported expression type for reduction: {expr}")
            return expr, []

        for old_pc, (instr, original_target) in enumerate(flatList):
            pc_map[old_pc] = len(three_ac_list)

            expanded_instrs = []

            if isinstance(instr, ChironAST.ProcedureDeclaration):
                if instr.name in self.sym_tab:
                    raise SyntaxError(f"Duplicate procedure declaration found: {instr.name}")
                self.sym_tab[instr.name] = {"entry" : len(three_ac_list)}
                expanded_instrs.append(instr)

            elif isinstance(instr, ChironAST.AssignmentCommand):
                res_var, expr_steps = reduce_expression(instr.rexpr)
                expanded_instrs.extend(expr_steps)
                expanded_instrs.append(ChironAST.AssignmentCommand(instr.lvar, res_var))
            elif isinstance(instr,  ChironAST.ConditionCommand):
                res_var, expr_steps = reduce_expression(instr.cond)
                expanded_instrs.extend(expr_steps)
                expanded_instrs.append(ChironAST.ConditionCommand(res_var))
            elif isinstance(instr, ChironAST.MoveCommand):
                res_var, expr_steps = reduce_expression(instr.expr)
                expanded_instrs.extend(expr_steps)
                expanded_instrs.append(ChironAST.MoveCommand(instr.direction, res_var))
            elif isinstance(instr, ChironAST.ProcedureCall):
                # Same arg reduction as above
                # print("DID WE GET HERE TOO?")
                reduced_args = []
                for arg in instr.args:
                    arg_var, arg_steps = reduce_expression(arg)
                    three_ac_list.extend([[s, -1] for s in arg_steps])
                    reduced_args.append(arg_var)

                for r_arg in reduced_args:
                    three_ac_list.append([ChironAST.ParamCommand(r_arg), -1])

                three_ac_list.append([ChironAST.CallN(instr.name, len(reduced_args)), target])
            # TODO: add other command types
            elif isinstance(instr, ChironAST.ReturnCommand):
                if instr.expr is not None:
                    res_var, expr_steps = reduce_expression(instr.expr)
                    expanded_instrs.extend(expr_steps)
                    expanded_instrs.append(ChironAST.ReturnCommand(res_var))
                else: # return void
                    expanded_instrs.append(instr)
            elif isinstance(instr, ChironAST.AssertCommand):
                # calculate assert output in temp
                # and add assert with that temp as condition
                cond_var, cond_instrs = reduce_expression(instr.cond)
                expanded_instrs.extend(cond_instrs)
                expanded_instrs.append(ChironAST.AssertCommand(cond_var))
            elif isinstance(instr, ChironAST.PrintCommand):
                res_var, expr_steps = reduce_expression(instr.expr)
                expanded_instrs.extend(expr_steps)
                expanded_instrs.append(ChironAST.PrintCommand(res_var))
            else:
                expanded_instrs.append(instr)

            for sub_instr in expanded_instrs:
                is_last = sub_instr == expanded_instrs[-1]
                is_proc_dec = isinstance(instr, ChironAST.ProcedureDeclaration) and sub_instr == expanded_instrs[0]
                target = original_target if (is_last or is_proc_dec) else -1
                three_ac_list.append([sub_instr, target])

        # Add mapping for the end of program (EOF)
        pc_map[len(flatList)] = len(three_ac_list)

        # Now that we know where every original instruction landed,
        # we update the targets in our 3AC list.
        for i in range(len(three_ac_list)):
            original_target = three_ac_list[i][1]

            if original_target == -1:
                # This was an intermediate temp assignment, just go to next line
                three_ac_list[i][1] = i + 1
            else:
                # This was a boundary instruction, jump to the mapped new_pc
                three_ac_list[i][1] = pc_map[original_target]

        # print("\n========== 3-Address Code IR ==========\n")
        # for idx, (instr, tgt) in enumerate(three_ac_list):
        #     print(f"[L{idx}]".rjust(5), f"\t{instr} [{tgt}]")
        return three_ac_list

    def checkTAC(self, three_ac_list):
        def get_all_locals(proc):
            all_offsets = dict()
            global_vars = set()
            local_vars = set()

            # params: negative offsets
            arg_count = len(proc.params)
            for i, param in enumerate(proc.params):
                p = param.replace(":", "")
                all_offsets[p] = -(arg_count - i) - 2  # Negative indices for parameters

            entry_pc = self.sym_tab[proc.name]["entry"]
            final_pc = three_ac_list[entry_pc][1]

            # print(f"Procedure '{proc.name}' parameters: {proc.params}")
            # print(f"start PC: {entry_pc}, final PC: {final_pc}\n")

            def l2g(expr):
                if isinstance(expr, ChironAST.Var):
                    expr_name = expr.varname.replace(":", "")
                    if expr_name in global_vars:
                        # print(f"Using global variable for reference to '{expr_name}' in procedure '{proc.name}'")
                        return ChironAST.Var("__g_" + expr_name)
                return expr
            
            for pc in range(entry_pc + 1, final_pc):
                stmt = three_ac_list[pc][0]

                if isinstance(stmt, ChironAST.GlobalDecl):
                    varname = stmt.varname.replace(":", "")
                    global_vars.add(varname)
                    # print(f"Found global variable declaration: '{varname}' in procedure '{proc.name}'")
                    continue

                if isinstance(stmt, ChironAST.AssignmentCommand):
                    lhs_name = stmt.lvar.varname.replace(":", "")
                    if lhs_name in global_vars:
                        three_ac_list[pc] = (ChironAST.AssignmentCommand(ChironAST.Var("__g_" + lhs_name), stmt.rexpr), three_ac_list[pc][1])
                        # print("Using global variable for assignment to '{lhs_name}' in procedure '{proc.name}'")
                    elif lhs_name not in local_vars and (":" + lhs_name) not in proc.params:
                        local_vars.add(lhs_name)
                        # print(f"Found assignment to '{lhs_name}' (will consider for local allocation)")

                    rhs_expr = stmt.rexpr
                        
                    if isinstance(rhs_expr, (ChironAST.BinArithOp, ChironAST.BinCondOp, ChironAST.AND, ChironAST.OR)):
                        r1 = rhs_expr.lexpr
                        r2 = rhs_expr.rexpr
                        three_ac_list[pc] = (ChironAST.AssignmentCommand(stmt.lvar, type(rhs_expr)(l2g(r1), l2g(r2))), three_ac_list[pc][1])

                    if isinstance(rhs_expr, (ChironAST.UnaryArithOp, ChironAST.NOT)):
                        r = rhs_expr.expr
                        three_ac_list[pc] = (ChironAST.AssignmentCommand(stmt.lvar, type(rhs_expr)(l2g(r))), three_ac_list[pc][1])

                if isinstance(stmt, ChironAST.ReturnCommand):
                    three_ac_list[pc] = (ChironAST.ReturnCommand(l2g(stmt.expr) if stmt.expr is not None else None), three_ac_list[pc][1])



            local_cnt = 0
            for var in local_vars:
                all_offsets[var] = local_cnt
                print(f"Assigning local offset {local_cnt} to variable '{var}' in procedure '{proc.name}'")
                local_cnt += 1

            return all_offsets

        idx = 0
        while idx < len(three_ac_list):
            instr, tgt = three_ac_list[idx]
            if isinstance(instr, ChironAST.ProcedureDeclaration):
                self.sym_tab[instr.name]["offsets"] = get_all_locals(instr)
                # print(f"Offsets for procedure '{instr.name}':")
                # for var, offset in self.sym_tab[instr.name]["offsets"].items():
                #     print(f"  {var}: {offset}")
                idx = tgt 
                self.fpc = tgt
            elif isinstance(instr, ChironAST.AssignmentCommand):
                lhs_name = instr.lvar.varname.replace(":", "")
                if lhs_name.startswith("__t"):
                    if self.sym_tab["_globals"]["offsets"].get(lhs_name) is None:
                        self.sym_tab["_globals"]["offsets"][lhs_name] = len(self.sym_tab["_globals"]["offsets"])
                idx += 1
            else:
                idx += 1


        # print("\n========== Updated 3AC IR ==========\n")
        # for idx, (instr, tgt) in enumerate(three_ac_list):
        #     # print(f"type: {type(instr)}")
        #     print(f"[L{idx}]".rjust(5), f"\t{instr} [{tgt}]")

        # print("\n========== 3-Address Code IR ==========\n")
        # for idx, (instr, tgt) in enumerate(three_ac_list):
        #     print(f"type: {type(instr)}")
        #     if isinstance(instr, ChironAST.AssignmentCommand):
        #         print(f"LHS: {instr.lvar}, RHS: {instr.rexpr}")
        #     print(f"[L{idx}]".rjust(5), f"\t{instr} [{tgt}]")
        return three_ac_list
