#!/usr/bin/env python3
from ChironAST import ChironAST
import linecache

class Debugger:
    """
    Simple textual gdb-like debugger for Chiron ConcreteInterpreter.

    Commands:
    c, continue        - resume execution until next breakpoint or program end
    s, step            - execute one instruction
    n, next            - alias for step (single instruction)
    r, regs [name]     - show all registers or a single register value
    b <L##|label|line> - set breakpoint at IR index L##, label name, or source line
    cl <L##|label|line>- clear breakpoint
    p <var>            - print variable value (accepts names with or without leading ':', temps like __t0, or __g_x globals)
    l, list [n]        - list IR around current pc (default 10 lines)
    bt                 - backtrace (call stack)
    h, help            - show help
    q, quit            - quit debugger (terminates program)
    """

    def __init__(self, interpreter):
        # interpreter: instance of ConcreteInterpreter
        self.inptr = interpreter
        self.breakpoints = set()
        self.step_mode = True
        self.source_file = self.inptr.args.progfl

        self.line_to_ir = {}
        for i, (instr, _) in enumerate(self.inptr.ir):
            # l = getattr(instr, "lineno", None)
            l = instr.lineno
            # We only store the FIRST IR index encountered for each source line
            if not l:
                raise ValueError(f"Instruction at IR index {i} is missing line number info: {instr}")

            if l not in self.line_to_ir:
                self.line_to_ir[l] = i

        self.sorted_lines = sorted(self.line_to_ir.keys())

    def _current_pc(self):
        return self.inptr.regs.pc

    def _instr_str(self, idx, instr, tgt):
        mark = "->" if idx == self._current_pc() else "  "
        bp_mark = "B" if idx in self.breakpoints else " "
        
        # 1. Format the Line Number
        lineno = getattr(instr, 'lineno', None)
        line_num_str = f"Line {lineno:<3}" if lineno else "        "
        
        # 2. Fetch the actual source text from the file
        source_text = ""
        source_text = linecache.getline(self.source_file, lineno).strip()
                
        display_source = (source_text[:27] + "...") if len(source_text) > 30 else source_text
        
        return f"{mark}{bp_mark} [L{idx:3}] {line_num_str} | {instr} [{tgt}] \t\t// {display_source:<30} "

    def print_current_instr(self):
        """Prints the instruction at the current Program Counter."""
        pc = self._current_pc()
        if pc < len(self.inptr.ir):
            instr, tgt = self.inptr.ir[pc]
            print(self._instr_str(pc, instr, tgt))

    def list_ins(self, window=10):
        pc = self._current_pc()
        start = max(0, pc - window // 2)
        end = min(len(self.inptr.ir), start + window)
        for i in range(start, end):
            instr, tgt = self.inptr.ir[i]
            print(self._instr_str(i, instr, tgt))

    def _resolve_target(self, arg):
        """Helper to resolve L## (IR index), digits (Source Line), or string (Label) to IR index."""
        # 1. Check for L## format (IR Index)
        if arg.upper().startswith("L") and arg[1:].isdigit():
            idx = int(arg[1:])
            if 0 <= idx < len(self.inptr.ir):
                return idx
            print(f"Invalid IR index: L{idx}")
            return None

        # 2. Check for numeric digits (Source Line Number)
        if arg.isdigit():
            line_val = int(arg)
            for i, (instr, _) in enumerate(self.inptr.ir):
                if hasattr(instr, "lineno") and instr.lineno == line_val:
                    return i
            print(f"Source line {line_val} not found.")
            return None

        # 3. Check for Label name
        for i, (instr, _) in enumerate(self.inptr.ir):
            if isinstance(instr, ChironAST.Label) and instr.name == arg:
                return i

        return None

    def set_breakpoint(self, arg):
        if not arg:
            print("Usage: b <L##|label|line>")
            return

        idx = self._resolve_target(arg)
        if idx is not None:
            self.breakpoints.add(idx)
            print(f"Breakpoint set at L{idx}")
        else:
            print(f"Target '{arg}' not found.")

    def clear_breakpoint(self, arg):
        if not arg:
            print("Usage: cl <L##|label|line>")
            return

        idx = self._resolve_target(arg)
        if idx is not None and idx in self.breakpoints:
            self.breakpoints.remove(idx)
            print(f"Cleared breakpoint at L{idx}")
        else:
            print(f"No matching breakpoint found for '{arg}'")

    def print_var(self, name):
        if not name:
            print("Usage: p <varname>")
            return
        vn = name.strip()
        # heuristics: temps and special names usually have no ':'
        if vn.startswith(":") or vn.startswith("__") or vn.startswith("__g_"):
            varnode = ChironAST.Var(vn)
        else:
            # prefer without colon for temps, otherwise try with colon for variables
            if vn.startswith("__"):
                varnode = ChironAST.Var(vn)
            else:
                # try global/local both: try with colon first
                varnode = ChironAST.Var(":" + vn)
        try:
            val = self.inptr.get_operand_value(varnode)
            print(f"{vn} = {val}")
        except Exception as e:
            print(f"Error evaluating '{vn}': {e}")

    def backtrace(self):
        # reconstruct call chain from stack using saved caller pcs and saved rbp
        frames = []
        bp = self.inptr.regs.bp
        while bp and bp > 1:
            # saved caller pc at bp-2, saved old bp at bp-1 (push order: pc, bp)
            try:
                caller_pc = self.inptr.stack.stack[bp - 2]
                old_bp = self.inptr.stack.stack[bp - 1]
            except Exception:
                break
            frames.append((caller_pc, old_bp))
            bp = old_bp
        if not frames:
            print("No frames (at top-level).")
            return
        for i, (caller_pc, old_bp) in enumerate(frames):
            func_instr = None
            if caller_pc and caller_pc - 1 < len(self.inptr.ir):
                func_instr = self.inptr.ir[caller_pc - 1][0]
            name = getattr(func_instr, "proc_name", getattr(func_instr, "name", "<unknown>"))
            print(f"#{i} pc={caller_pc} proc={name}")

    def _run_one(self):
        try:
            finished = self.inptr.interpret()
            return finished
        except Exception as e:
            print("Runtime error during execution:", e)
            return True  # stop debugger on runtime error

    def next_step(self):
        """
        Step over: run until the current instruction has been executed and
        any called routines have returned (i.e. bp <= start_bp and pc moved).
        This implements 'next' (like gdb 'next') vs 'step' which steps into calls.
        """
        start_pc = self._current_pc()
        start_bp = getattr(self.inptr.regs, "bp", 0)
        # If no meaningful bp, just do one step.
        if not start_bp:
            finished = self._run_one()
            return finished

        while True:
            # Single instruction
            finished = self._run_one()
            if finished:
                print("Program ended.")
                return True
            pc = self._current_pc()
            bp = getattr(self.inptr.regs, "bp", 0)

            # print(f"Debug: next_step loop: pc={pc}, bp={bp}, start_pc={start_pc}, start_bp={start_bp}")

            # Stop if we've moved past the original instruction and bp indicates we're at/above original frame
            if pc != start_pc and bp < start_bp:
                break
            # Also stop if we hit a user breakpoint (pause before executing it)
            if pc in self.breakpoints:
                print(f"Hit breakpoint at L{pc}")
                # self.list_ins(10)
                break
        return False

    def print_regs(self, name=None):
        """
        Print registers. If name is provided, print only that register.
        """
        regs = self.inptr.regs
        # Try to get a mapping of attributes
        try:
            items = vars(regs)
        except TypeError:
            # fallback: collect public non-callable attributes
            items = {}
            for k in dir(regs):
                if k.startswith("_"):
                    continue
                try:
                    v = getattr(regs, k)
                except Exception:
                    continue
                if callable(v):
                    continue
                items[k] = v
        if name:
            key = name
            if key in items:
                print(f"{key} = {items[key]}")
            else:
                # try numeric names (e.g., 'pc') via getattr as a last resort
                try:
                    val = getattr(regs, key)
                    print(f"{key} = {val}")
                except Exception:
                    print(f"No such register '{key}'")
            return
        # print all registers sorted
        for k in sorted(items.keys()):
            print(f"{k} = {items[k]}")

    def run(self):
        print("Starting debugger. Type 'h' for help.")
        # If starting PC already at breakpoint, stop before first instruction.
        if self._current_pc() in self.breakpoints:
            print(f"Hit breakpoint at L{self._current_pc()}")
            self.list_ins(10)

        while True:
            # pause if at breakpoint
            if self._current_pc() in self.breakpoints:
                print(f"Hit breakpoint at L{self._current_pc()}")
                self.list_ins(10)
                self.step_mode = True

            if not self.step_mode:
                # run until next breakpoint or end
                finished = False
                while True:
                    finished = self._run_one()
                    if finished:
                        print("Program ended.")
                        return
                    if self._current_pc() in self.breakpoints:                        
                        print(f"Hit breakpoint at L{self._current_pc()}")
                        self.print_current_instr() 
                        break
                # now loop to REPL
            # Enter REPL for commands
            try:
                cmdline = input("(chiron-db) ").strip()
            except (EOFError, KeyboardInterrupt):
                print("quit")
                return
            if not cmdline:
                continue
            parts = cmdline.split()
            cmd = parts[0]
            args = parts[1:] if len(parts) > 1 else []
            if cmd in ("c", "continue"):
                self.step_mode = False
                # continue main loop will resume execution
                finished = self._run_one()
                if finished:
                    print("Program ended.")
                    return
                # If the NEXT instruction is also a breakpoint, stop immediately
                if self._current_pc() in self.breakpoints:
                    print(f"Hit breakpoint at [L{self._current_pc()}]")
                    self.print_current_instr()
                    self.step_mode = True
                continue
            elif cmd in ("s", "step"):
                self.step_mode = True
                finished = self._run_one()
                if finished:
                    print("Program ended.")
                    return
                self.print_current_instr()  
                continue
            elif cmd in ("n", "next"):
                # 'next' steps over calls
                self.step_mode = True
                finished = self.next_step()
                if finished:
                    return
                self.print_current_instr()  
                continue
            elif cmd in ("b", "break"):
                if not args:
                    print("Usage: b <L##|label|line>")
                else:
                    self.set_breakpoint(args[0])
                continue
            elif cmd == "cl":
                if not args:
                    print("Usage: cl <L##|label|line>")
                else:
                    self.clear_breakpoint(args[0])
                continue
            elif cmd in ("p", "print"):
                if not args:
                    print("Usage: p <varname>")
                else:
                    self.print_var(args[0])
                continue
            elif cmd in ("l", "list"):
                n = int(args[0]) if args and args[0].isdigit() else 10
                self.list_ins(n)
                continue
            elif cmd in ("bt", "where"):
                self.backtrace()
                continue
            elif cmd in ("h", "help"):
                print(self.__doc__)
                continue
            elif cmd in ("q", "quit"):
                print("Quitting debugger.")
                return
            elif cmd in ("r", "regs"):
                # show all registers or a specific one if provided
                if args:
                    self.print_regs(args[0])
                else:
                    self.print_regs()
                continue
            else:
                print("Unknown command. Type 'h' for help.")
