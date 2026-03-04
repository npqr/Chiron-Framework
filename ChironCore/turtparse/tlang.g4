grammar tlang;

start : instruction_list EOF
      ;

instruction_list : (instruction)*
		 ;

strict_ilist : (instruction)+
             ;

instruction : assignment
	    | conditional
	    | loop
	    | moveCommand
	    | penCommand
	    | gotoCommand
	    | pauseCommand
	    | procedureDeclaration
		| procedureCall
		| assertCommand
        | returnCommand
        | printCommand    
	    ;

assertCommand : 'assert' (condition | expression) ;

conditional : ifConditional | ifElseConditional ;

ifConditional : 'if' (condition | expression) '[' strict_ilist ']' ;

ifElseConditional : 'if' (condition | expression) '[' strict_ilist ']' 'else' '[' strict_ilist ']' ;

loop : 'repeat' value '[' strict_ilist ']' ;

gotoCommand : 'goto' '(' expression ',' expression ')';

assignment : VAR '=' expression
	   ;

moveCommand : moveOp expression ;
moveOp : 'forward' | 'backward' | 'left' | 'right' ;

penCommand : 'penup' | 'pendown' ;

pauseCommand : 'pause' ;

procedureDeclaration : 'to' NAME '(' paramList? ')' '[' instruction_list ']' ;

paramList : VAR (',' VAR)* ;

procedureCall : NAME '(' argList? ')' ;

argList : expression (',' expression)* ;

expression : 
             unaryArithOp expression               #unaryExpr
           | expression multiplicative expression  #mulExpr
		   | expression additive expression        #addExpr
		   | value                                 #valueExpr
           | procedureCall						   #procedureCallExpr
		   | '(' expression ')'                    #parenExpr
 	   ;

multiplicative : MUL | DIV;
additive : PLUS | MINUS;

unaryArithOp : MINUS ;

PLUS     : '+' ;
MINUS    : '-' ;
MUL  	 : '*' ;
DIV      : '/' ;


// TODO :
// procedure_declaration : 'to' NAME (VAR)+ strict_ilist 'end' ;

condition : NOT condition
          |expression binCondOp expression
	  | condition logicOp condition
	  | PENCOND
	  | '(' condition ')'
	  ;


binCondOp :  EQ | NEQ | LT | GT | LTE | GTE
	 ;

logicOp : AND | OR ;

PENCOND : 'pendown?';
LT : '<' ;
GT : '>' ;
EQ : '==';
NEQ: '!=';
LTE: '<=';
GTE: '>=';
AND: '&&';
OR : '||';
NOT: '!' ;

value : NUM
      | VAR
      ;

NUM  : [0-9]+        ;

VAR  : ':'[a-zA-Z_] [a-zA-Z0-9]* ;

NAME : [a-zA-Z]+     ;

Whitespace: [ \t\n\r]+ -> skip;

COMMENT : '//' ~[\r\n]* -> skip; 
MULTILINE_COMMENT : '/*' .*? '*/' -> skip; 

returnCommand : 'return' | 'return ' expression ;

printCommand : 'print' expression ;

