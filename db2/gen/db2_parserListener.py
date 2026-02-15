# Generated from C:/Users/natar/AI/AS400Parser/grammars/db2_parser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .db2_parser import db2_parser
else:
    from db2_parser import db2_parser

# This class defines a complete listener for a parse tree produced by db2_parser.
class db2_parserListener(ParseTreeListener):

    # Enter a parse tree produced by db2_parser#sqlScript.
    def enterSqlScript(self, ctx:db2_parser.SqlScriptContext):
        pass

    # Exit a parse tree produced by db2_parser#sqlScript.
    def exitSqlScript(self, ctx:db2_parser.SqlScriptContext):
        pass


    # Enter a parse tree produced by db2_parser#sqlStatement.
    def enterSqlStatement(self, ctx:db2_parser.SqlStatementContext):
        pass

    # Exit a parse tree produced by db2_parser#sqlStatement.
    def exitSqlStatement(self, ctx:db2_parser.SqlStatementContext):
        pass


    # Enter a parse tree produced by db2_parser#semicolon.
    def enterSemicolon(self, ctx:db2_parser.SemicolonContext):
        pass

    # Exit a parse tree produced by db2_parser#semicolon.
    def exitSemicolon(self, ctx:db2_parser.SemicolonContext):
        pass


    # Enter a parse tree produced by db2_parser#selectStatement.
    def enterSelectStatement(self, ctx:db2_parser.SelectStatementContext):
        pass

    # Exit a parse tree produced by db2_parser#selectStatement.
    def exitSelectStatement(self, ctx:db2_parser.SelectStatementContext):
        pass


    # Enter a parse tree produced by db2_parser#selectList.
    def enterSelectList(self, ctx:db2_parser.SelectListContext):
        pass

    # Exit a parse tree produced by db2_parser#selectList.
    def exitSelectList(self, ctx:db2_parser.SelectListContext):
        pass


    # Enter a parse tree produced by db2_parser#selectItem.
    def enterSelectItem(self, ctx:db2_parser.SelectItemContext):
        pass

    # Exit a parse tree produced by db2_parser#selectItem.
    def exitSelectItem(self, ctx:db2_parser.SelectItemContext):
        pass


    # Enter a parse tree produced by db2_parser#alias.
    def enterAlias(self, ctx:db2_parser.AliasContext):
        pass

    # Exit a parse tree produced by db2_parser#alias.
    def exitAlias(self, ctx:db2_parser.AliasContext):
        pass


    # Enter a parse tree produced by db2_parser#tableExpression.
    def enterTableExpression(self, ctx:db2_parser.TableExpressionContext):
        pass

    # Exit a parse tree produced by db2_parser#tableExpression.
    def exitTableExpression(self, ctx:db2_parser.TableExpressionContext):
        pass


    # Enter a parse tree produced by db2_parser#tableReference.
    def enterTableReference(self, ctx:db2_parser.TableReferenceContext):
        pass

    # Exit a parse tree produced by db2_parser#tableReference.
    def exitTableReference(self, ctx:db2_parser.TableReferenceContext):
        pass


    # Enter a parse tree produced by db2_parser#tableFunctionName.
    def enterTableFunctionName(self, ctx:db2_parser.TableFunctionNameContext):
        pass

    # Exit a parse tree produced by db2_parser#tableFunctionName.
    def exitTableFunctionName(self, ctx:db2_parser.TableFunctionNameContext):
        pass


    # Enter a parse tree produced by db2_parser#viewName.
    def enterViewName(self, ctx:db2_parser.ViewNameContext):
        pass

    # Exit a parse tree produced by db2_parser#viewName.
    def exitViewName(self, ctx:db2_parser.ViewNameContext):
        pass


    # Enter a parse tree produced by db2_parser#indexName.
    def enterIndexName(self, ctx:db2_parser.IndexNameContext):
        pass

    # Exit a parse tree produced by db2_parser#indexName.
    def exitIndexName(self, ctx:db2_parser.IndexNameContext):
        pass


    # Enter a parse tree produced by db2_parser#sequenceName.
    def enterSequenceName(self, ctx:db2_parser.SequenceNameContext):
        pass

    # Exit a parse tree produced by db2_parser#sequenceName.
    def exitSequenceName(self, ctx:db2_parser.SequenceNameContext):
        pass


    # Enter a parse tree produced by db2_parser#joinClause.
    def enterJoinClause(self, ctx:db2_parser.JoinClauseContext):
        pass

    # Exit a parse tree produced by db2_parser#joinClause.
    def exitJoinClause(self, ctx:db2_parser.JoinClauseContext):
        pass


    # Enter a parse tree produced by db2_parser#joinCondition.
    def enterJoinCondition(self, ctx:db2_parser.JoinConditionContext):
        pass

    # Exit a parse tree produced by db2_parser#joinCondition.
    def exitJoinCondition(self, ctx:db2_parser.JoinConditionContext):
        pass


    # Enter a parse tree produced by db2_parser#columnList.
    def enterColumnList(self, ctx:db2_parser.ColumnListContext):
        pass

    # Exit a parse tree produced by db2_parser#columnList.
    def exitColumnList(self, ctx:db2_parser.ColumnListContext):
        pass


    # Enter a parse tree produced by db2_parser#whereClause.
    def enterWhereClause(self, ctx:db2_parser.WhereClauseContext):
        pass

    # Exit a parse tree produced by db2_parser#whereClause.
    def exitWhereClause(self, ctx:db2_parser.WhereClauseContext):
        pass


    # Enter a parse tree produced by db2_parser#groupByClause.
    def enterGroupByClause(self, ctx:db2_parser.GroupByClauseContext):
        pass

    # Exit a parse tree produced by db2_parser#groupByClause.
    def exitGroupByClause(self, ctx:db2_parser.GroupByClauseContext):
        pass


    # Enter a parse tree produced by db2_parser#havingClause.
    def enterHavingClause(self, ctx:db2_parser.HavingClauseContext):
        pass

    # Exit a parse tree produced by db2_parser#havingClause.
    def exitHavingClause(self, ctx:db2_parser.HavingClauseContext):
        pass


    # Enter a parse tree produced by db2_parser#orderByClause.
    def enterOrderByClause(self, ctx:db2_parser.OrderByClauseContext):
        pass

    # Exit a parse tree produced by db2_parser#orderByClause.
    def exitOrderByClause(self, ctx:db2_parser.OrderByClauseContext):
        pass


    # Enter a parse tree produced by db2_parser#orderByItem.
    def enterOrderByItem(self, ctx:db2_parser.OrderByItemContext):
        pass

    # Exit a parse tree produced by db2_parser#orderByItem.
    def exitOrderByItem(self, ctx:db2_parser.OrderByItemContext):
        pass


    # Enter a parse tree produced by db2_parser#limitClause.
    def enterLimitClause(self, ctx:db2_parser.LimitClauseContext):
        pass

    # Exit a parse tree produced by db2_parser#limitClause.
    def exitLimitClause(self, ctx:db2_parser.LimitClauseContext):
        pass


    # Enter a parse tree produced by db2_parser#offsetClause.
    def enterOffsetClause(self, ctx:db2_parser.OffsetClauseContext):
        pass

    # Exit a parse tree produced by db2_parser#offsetClause.
    def exitOffsetClause(self, ctx:db2_parser.OffsetClauseContext):
        pass


    # Enter a parse tree produced by db2_parser#fetchClause.
    def enterFetchClause(self, ctx:db2_parser.FetchClauseContext):
        pass

    # Exit a parse tree produced by db2_parser#fetchClause.
    def exitFetchClause(self, ctx:db2_parser.FetchClauseContext):
        pass


    # Enter a parse tree produced by db2_parser#insertStatement.
    def enterInsertStatement(self, ctx:db2_parser.InsertStatementContext):
        pass

    # Exit a parse tree produced by db2_parser#insertStatement.
    def exitInsertStatement(self, ctx:db2_parser.InsertStatementContext):
        pass


    # Enter a parse tree produced by db2_parser#valueList.
    def enterValueList(self, ctx:db2_parser.ValueListContext):
        pass

    # Exit a parse tree produced by db2_parser#valueList.
    def exitValueList(self, ctx:db2_parser.ValueListContext):
        pass


    # Enter a parse tree produced by db2_parser#arguments.
    def enterArguments(self, ctx:db2_parser.ArgumentsContext):
        pass

    # Exit a parse tree produced by db2_parser#arguments.
    def exitArguments(self, ctx:db2_parser.ArgumentsContext):
        pass


    # Enter a parse tree produced by db2_parser#updateStatement.
    def enterUpdateStatement(self, ctx:db2_parser.UpdateStatementContext):
        pass

    # Exit a parse tree produced by db2_parser#updateStatement.
    def exitUpdateStatement(self, ctx:db2_parser.UpdateStatementContext):
        pass


    # Enter a parse tree produced by db2_parser#setClause.
    def enterSetClause(self, ctx:db2_parser.SetClauseContext):
        pass

    # Exit a parse tree produced by db2_parser#setClause.
    def exitSetClause(self, ctx:db2_parser.SetClauseContext):
        pass


    # Enter a parse tree produced by db2_parser#deleteStatement.
    def enterDeleteStatement(self, ctx:db2_parser.DeleteStatementContext):
        pass

    # Exit a parse tree produced by db2_parser#deleteStatement.
    def exitDeleteStatement(self, ctx:db2_parser.DeleteStatementContext):
        pass


    # Enter a parse tree produced by db2_parser#mergeStatement.
    def enterMergeStatement(self, ctx:db2_parser.MergeStatementContext):
        pass

    # Exit a parse tree produced by db2_parser#mergeStatement.
    def exitMergeStatement(self, ctx:db2_parser.MergeStatementContext):
        pass


    # Enter a parse tree produced by db2_parser#mergeCondition.
    def enterMergeCondition(self, ctx:db2_parser.MergeConditionContext):
        pass

    # Exit a parse tree produced by db2_parser#mergeCondition.
    def exitMergeCondition(self, ctx:db2_parser.MergeConditionContext):
        pass


    # Enter a parse tree produced by db2_parser#updateClause.
    def enterUpdateClause(self, ctx:db2_parser.UpdateClauseContext):
        pass

    # Exit a parse tree produced by db2_parser#updateClause.
    def exitUpdateClause(self, ctx:db2_parser.UpdateClauseContext):
        pass


    # Enter a parse tree produced by db2_parser#insertClause.
    def enterInsertClause(self, ctx:db2_parser.InsertClauseContext):
        pass

    # Exit a parse tree produced by db2_parser#insertClause.
    def exitInsertClause(self, ctx:db2_parser.InsertClauseContext):
        pass


    # Enter a parse tree produced by db2_parser#createStatement.
    def enterCreateStatement(self, ctx:db2_parser.CreateStatementContext):
        pass

    # Exit a parse tree produced by db2_parser#createStatement.
    def exitCreateStatement(self, ctx:db2_parser.CreateStatementContext):
        pass


    # Enter a parse tree produced by db2_parser#createTableStatement.
    def enterCreateTableStatement(self, ctx:db2_parser.CreateTableStatementContext):
        pass

    # Exit a parse tree produced by db2_parser#createTableStatement.
    def exitCreateTableStatement(self, ctx:db2_parser.CreateTableStatementContext):
        pass


    # Enter a parse tree produced by db2_parser#columnDefinition.
    def enterColumnDefinition(self, ctx:db2_parser.ColumnDefinitionContext):
        pass

    # Exit a parse tree produced by db2_parser#columnDefinition.
    def exitColumnDefinition(self, ctx:db2_parser.ColumnDefinitionContext):
        pass


    # Enter a parse tree produced by db2_parser#dataType.
    def enterDataType(self, ctx:db2_parser.DataTypeContext):
        pass

    # Exit a parse tree produced by db2_parser#dataType.
    def exitDataType(self, ctx:db2_parser.DataTypeContext):
        pass


    # Enter a parse tree produced by db2_parser#precision.
    def enterPrecision(self, ctx:db2_parser.PrecisionContext):
        pass

    # Exit a parse tree produced by db2_parser#precision.
    def exitPrecision(self, ctx:db2_parser.PrecisionContext):
        pass


    # Enter a parse tree produced by db2_parser#scale.
    def enterScale(self, ctx:db2_parser.ScaleContext):
        pass

    # Exit a parse tree produced by db2_parser#scale.
    def exitScale(self, ctx:db2_parser.ScaleContext):
        pass


    # Enter a parse tree produced by db2_parser#length.
    def enterLength(self, ctx:db2_parser.LengthContext):
        pass

    # Exit a parse tree produced by db2_parser#length.
    def exitLength(self, ctx:db2_parser.LengthContext):
        pass


    # Enter a parse tree produced by db2_parser#columnConstraint.
    def enterColumnConstraint(self, ctx:db2_parser.ColumnConstraintContext):
        pass

    # Exit a parse tree produced by db2_parser#columnConstraint.
    def exitColumnConstraint(self, ctx:db2_parser.ColumnConstraintContext):
        pass


    # Enter a parse tree produced by db2_parser#defaultValue.
    def enterDefaultValue(self, ctx:db2_parser.DefaultValueContext):
        pass

    # Exit a parse tree produced by db2_parser#defaultValue.
    def exitDefaultValue(self, ctx:db2_parser.DefaultValueContext):
        pass


    # Enter a parse tree produced by db2_parser#checkCondition.
    def enterCheckCondition(self, ctx:db2_parser.CheckConditionContext):
        pass

    # Exit a parse tree produced by db2_parser#checkCondition.
    def exitCheckCondition(self, ctx:db2_parser.CheckConditionContext):
        pass


    # Enter a parse tree produced by db2_parser#createViewStatement.
    def enterCreateViewStatement(self, ctx:db2_parser.CreateViewStatementContext):
        pass

    # Exit a parse tree produced by db2_parser#createViewStatement.
    def exitCreateViewStatement(self, ctx:db2_parser.CreateViewStatementContext):
        pass


    # Enter a parse tree produced by db2_parser#createIndexStatement.
    def enterCreateIndexStatement(self, ctx:db2_parser.CreateIndexStatementContext):
        pass

    # Exit a parse tree produced by db2_parser#createIndexStatement.
    def exitCreateIndexStatement(self, ctx:db2_parser.CreateIndexStatementContext):
        pass


    # Enter a parse tree produced by db2_parser#createSequenceStatement.
    def enterCreateSequenceStatement(self, ctx:db2_parser.CreateSequenceStatementContext):
        pass

    # Exit a parse tree produced by db2_parser#createSequenceStatement.
    def exitCreateSequenceStatement(self, ctx:db2_parser.CreateSequenceStatementContext):
        pass


    # Enter a parse tree produced by db2_parser#startValue.
    def enterStartValue(self, ctx:db2_parser.StartValueContext):
        pass

    # Exit a parse tree produced by db2_parser#startValue.
    def exitStartValue(self, ctx:db2_parser.StartValueContext):
        pass


    # Enter a parse tree produced by db2_parser#incrementValue.
    def enterIncrementValue(self, ctx:db2_parser.IncrementValueContext):
        pass

    # Exit a parse tree produced by db2_parser#incrementValue.
    def exitIncrementValue(self, ctx:db2_parser.IncrementValueContext):
        pass


    # Enter a parse tree produced by db2_parser#minValue.
    def enterMinValue(self, ctx:db2_parser.MinValueContext):
        pass

    # Exit a parse tree produced by db2_parser#minValue.
    def exitMinValue(self, ctx:db2_parser.MinValueContext):
        pass


    # Enter a parse tree produced by db2_parser#maxValue.
    def enterMaxValue(self, ctx:db2_parser.MaxValueContext):
        pass

    # Exit a parse tree produced by db2_parser#maxValue.
    def exitMaxValue(self, ctx:db2_parser.MaxValueContext):
        pass


    # Enter a parse tree produced by db2_parser#alterStatement.
    def enterAlterStatement(self, ctx:db2_parser.AlterStatementContext):
        pass

    # Exit a parse tree produced by db2_parser#alterStatement.
    def exitAlterStatement(self, ctx:db2_parser.AlterStatementContext):
        pass


    # Enter a parse tree produced by db2_parser#alterAction.
    def enterAlterAction(self, ctx:db2_parser.AlterActionContext):
        pass

    # Exit a parse tree produced by db2_parser#alterAction.
    def exitAlterAction(self, ctx:db2_parser.AlterActionContext):
        pass


    # Enter a parse tree produced by db2_parser#constraintName.
    def enterConstraintName(self, ctx:db2_parser.ConstraintNameContext):
        pass

    # Exit a parse tree produced by db2_parser#constraintName.
    def exitConstraintName(self, ctx:db2_parser.ConstraintNameContext):
        pass


    # Enter a parse tree produced by db2_parser#constraintDefinition.
    def enterConstraintDefinition(self, ctx:db2_parser.ConstraintDefinitionContext):
        pass

    # Exit a parse tree produced by db2_parser#constraintDefinition.
    def exitConstraintDefinition(self, ctx:db2_parser.ConstraintDefinitionContext):
        pass


    # Enter a parse tree produced by db2_parser#dropStatement.
    def enterDropStatement(self, ctx:db2_parser.DropStatementContext):
        pass

    # Exit a parse tree produced by db2_parser#dropStatement.
    def exitDropStatement(self, ctx:db2_parser.DropStatementContext):
        pass


    # Enter a parse tree produced by db2_parser#objectName.
    def enterObjectName(self, ctx:db2_parser.ObjectNameContext):
        pass

    # Exit a parse tree produced by db2_parser#objectName.
    def exitObjectName(self, ctx:db2_parser.ObjectNameContext):
        pass


    # Enter a parse tree produced by db2_parser#grantStatement.
    def enterGrantStatement(self, ctx:db2_parser.GrantStatementContext):
        pass

    # Exit a parse tree produced by db2_parser#grantStatement.
    def exitGrantStatement(self, ctx:db2_parser.GrantStatementContext):
        pass


    # Enter a parse tree produced by db2_parser#privilegeList.
    def enterPrivilegeList(self, ctx:db2_parser.PrivilegeListContext):
        pass

    # Exit a parse tree produced by db2_parser#privilegeList.
    def exitPrivilegeList(self, ctx:db2_parser.PrivilegeListContext):
        pass


    # Enter a parse tree produced by db2_parser#privilege.
    def enterPrivilege(self, ctx:db2_parser.PrivilegeContext):
        pass

    # Exit a parse tree produced by db2_parser#privilege.
    def exitPrivilege(self, ctx:db2_parser.PrivilegeContext):
        pass


    # Enter a parse tree produced by db2_parser#objectType.
    def enterObjectType(self, ctx:db2_parser.ObjectTypeContext):
        pass

    # Exit a parse tree produced by db2_parser#objectType.
    def exitObjectType(self, ctx:db2_parser.ObjectTypeContext):
        pass


    # Enter a parse tree produced by db2_parser#granteeList.
    def enterGranteeList(self, ctx:db2_parser.GranteeListContext):
        pass

    # Exit a parse tree produced by db2_parser#granteeList.
    def exitGranteeList(self, ctx:db2_parser.GranteeListContext):
        pass


    # Enter a parse tree produced by db2_parser#grantee.
    def enterGrantee(self, ctx:db2_parser.GranteeContext):
        pass

    # Exit a parse tree produced by db2_parser#grantee.
    def exitGrantee(self, ctx:db2_parser.GranteeContext):
        pass


    # Enter a parse tree produced by db2_parser#revokeStatement.
    def enterRevokeStatement(self, ctx:db2_parser.RevokeStatementContext):
        pass

    # Exit a parse tree produced by db2_parser#revokeStatement.
    def exitRevokeStatement(self, ctx:db2_parser.RevokeStatementContext):
        pass


    # Enter a parse tree produced by db2_parser#commitStatement.
    def enterCommitStatement(self, ctx:db2_parser.CommitStatementContext):
        pass

    # Exit a parse tree produced by db2_parser#commitStatement.
    def exitCommitStatement(self, ctx:db2_parser.CommitStatementContext):
        pass


    # Enter a parse tree produced by db2_parser#rollbackStatement.
    def enterRollbackStatement(self, ctx:db2_parser.RollbackStatementContext):
        pass

    # Exit a parse tree produced by db2_parser#rollbackStatement.
    def exitRollbackStatement(self, ctx:db2_parser.RollbackStatementContext):
        pass


    # Enter a parse tree produced by db2_parser#beginStatement.
    def enterBeginStatement(self, ctx:db2_parser.BeginStatementContext):
        pass

    # Exit a parse tree produced by db2_parser#beginStatement.
    def exitBeginStatement(self, ctx:db2_parser.BeginStatementContext):
        pass


    # Enter a parse tree produced by db2_parser#savepointName.
    def enterSavepointName(self, ctx:db2_parser.SavepointNameContext):
        pass

    # Exit a parse tree produced by db2_parser#savepointName.
    def exitSavepointName(self, ctx:db2_parser.SavepointNameContext):
        pass


    # Enter a parse tree produced by db2_parser#setStatement.
    def enterSetStatement(self, ctx:db2_parser.SetStatementContext):
        pass

    # Exit a parse tree produced by db2_parser#setStatement.
    def exitSetStatement(self, ctx:db2_parser.SetStatementContext):
        pass


    # Enter a parse tree produced by db2_parser#optionName.
    def enterOptionName(self, ctx:db2_parser.OptionNameContext):
        pass

    # Exit a parse tree produced by db2_parser#optionName.
    def exitOptionName(self, ctx:db2_parser.OptionNameContext):
        pass


    # Enter a parse tree produced by db2_parser#optionValue.
    def enterOptionValue(self, ctx:db2_parser.OptionValueContext):
        pass

    # Exit a parse tree produced by db2_parser#optionValue.
    def exitOptionValue(self, ctx:db2_parser.OptionValueContext):
        pass


    # Enter a parse tree produced by db2_parser#commentStatement.
    def enterCommentStatement(self, ctx:db2_parser.CommentStatementContext):
        pass

    # Exit a parse tree produced by db2_parser#commentStatement.
    def exitCommentStatement(self, ctx:db2_parser.CommentStatementContext):
        pass


    # Enter a parse tree produced by db2_parser#expression.
    def enterExpression(self, ctx:db2_parser.ExpressionContext):
        pass

    # Exit a parse tree produced by db2_parser#expression.
    def exitExpression(self, ctx:db2_parser.ExpressionContext):
        pass


    # Enter a parse tree produced by db2_parser#primaryExpression.
    def enterPrimaryExpression(self, ctx:db2_parser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by db2_parser#primaryExpression.
    def exitPrimaryExpression(self, ctx:db2_parser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by db2_parser#literal.
    def enterLiteral(self, ctx:db2_parser.LiteralContext):
        pass

    # Exit a parse tree produced by db2_parser#literal.
    def exitLiteral(self, ctx:db2_parser.LiteralContext):
        pass


    # Enter a parse tree produced by db2_parser#columnReference.
    def enterColumnReference(self, ctx:db2_parser.ColumnReferenceContext):
        pass

    # Exit a parse tree produced by db2_parser#columnReference.
    def exitColumnReference(self, ctx:db2_parser.ColumnReferenceContext):
        pass


    # Enter a parse tree produced by db2_parser#tableName.
    def enterTableName(self, ctx:db2_parser.TableNameContext):
        pass

    # Exit a parse tree produced by db2_parser#tableName.
    def exitTableName(self, ctx:db2_parser.TableNameContext):
        pass


    # Enter a parse tree produced by db2_parser#columnName.
    def enterColumnName(self, ctx:db2_parser.ColumnNameContext):
        pass

    # Exit a parse tree produced by db2_parser#columnName.
    def exitColumnName(self, ctx:db2_parser.ColumnNameContext):
        pass


    # Enter a parse tree produced by db2_parser#parameter.
    def enterParameter(self, ctx:db2_parser.ParameterContext):
        pass

    # Exit a parse tree produced by db2_parser#parameter.
    def exitParameter(self, ctx:db2_parser.ParameterContext):
        pass


    # Enter a parse tree produced by db2_parser#operator.
    def enterOperator(self, ctx:db2_parser.OperatorContext):
        pass

    # Exit a parse tree produced by db2_parser#operator.
    def exitOperator(self, ctx:db2_parser.OperatorContext):
        pass


    # Enter a parse tree produced by db2_parser#arithmeticOperator.
    def enterArithmeticOperator(self, ctx:db2_parser.ArithmeticOperatorContext):
        pass

    # Exit a parse tree produced by db2_parser#arithmeticOperator.
    def exitArithmeticOperator(self, ctx:db2_parser.ArithmeticOperatorContext):
        pass


    # Enter a parse tree produced by db2_parser#comparisonOperator.
    def enterComparisonOperator(self, ctx:db2_parser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by db2_parser#comparisonOperator.
    def exitComparisonOperator(self, ctx:db2_parser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by db2_parser#logicalOperator.
    def enterLogicalOperator(self, ctx:db2_parser.LogicalOperatorContext):
        pass

    # Exit a parse tree produced by db2_parser#logicalOperator.
    def exitLogicalOperator(self, ctx:db2_parser.LogicalOperatorContext):
        pass


    # Enter a parse tree produced by db2_parser#functionCall.
    def enterFunctionCall(self, ctx:db2_parser.FunctionCallContext):
        pass

    # Exit a parse tree produced by db2_parser#functionCall.
    def exitFunctionCall(self, ctx:db2_parser.FunctionCallContext):
        pass


    # Enter a parse tree produced by db2_parser#functionName.
    def enterFunctionName(self, ctx:db2_parser.FunctionNameContext):
        pass

    # Exit a parse tree produced by db2_parser#functionName.
    def exitFunctionName(self, ctx:db2_parser.FunctionNameContext):
        pass


    # Enter a parse tree produced by db2_parser#argumentList.
    def enterArgumentList(self, ctx:db2_parser.ArgumentListContext):
        pass

    # Exit a parse tree produced by db2_parser#argumentList.
    def exitArgumentList(self, ctx:db2_parser.ArgumentListContext):
        pass


    # Enter a parse tree produced by db2_parser#windowFunction.
    def enterWindowFunction(self, ctx:db2_parser.WindowFunctionContext):
        pass

    # Exit a parse tree produced by db2_parser#windowFunction.
    def exitWindowFunction(self, ctx:db2_parser.WindowFunctionContext):
        pass


    # Enter a parse tree produced by db2_parser#windowFunctionName.
    def enterWindowFunctionName(self, ctx:db2_parser.WindowFunctionNameContext):
        pass

    # Exit a parse tree produced by db2_parser#windowFunctionName.
    def exitWindowFunctionName(self, ctx:db2_parser.WindowFunctionNameContext):
        pass


    # Enter a parse tree produced by db2_parser#windowSpecification.
    def enterWindowSpecification(self, ctx:db2_parser.WindowSpecificationContext):
        pass

    # Exit a parse tree produced by db2_parser#windowSpecification.
    def exitWindowSpecification(self, ctx:db2_parser.WindowSpecificationContext):
        pass


    # Enter a parse tree produced by db2_parser#frameSpecification.
    def enterFrameSpecification(self, ctx:db2_parser.FrameSpecificationContext):
        pass

    # Exit a parse tree produced by db2_parser#frameSpecification.
    def exitFrameSpecification(self, ctx:db2_parser.FrameSpecificationContext):
        pass


    # Enter a parse tree produced by db2_parser#frameStart.
    def enterFrameStart(self, ctx:db2_parser.FrameStartContext):
        pass

    # Exit a parse tree produced by db2_parser#frameStart.
    def exitFrameStart(self, ctx:db2_parser.FrameStartContext):
        pass


    # Enter a parse tree produced by db2_parser#frameEnd.
    def enterFrameEnd(self, ctx:db2_parser.FrameEndContext):
        pass

    # Exit a parse tree produced by db2_parser#frameEnd.
    def exitFrameEnd(self, ctx:db2_parser.FrameEndContext):
        pass


    # Enter a parse tree produced by db2_parser#caseExpression.
    def enterCaseExpression(self, ctx:db2_parser.CaseExpressionContext):
        pass

    # Exit a parse tree produced by db2_parser#caseExpression.
    def exitCaseExpression(self, ctx:db2_parser.CaseExpressionContext):
        pass


    # Enter a parse tree produced by db2_parser#whenClause.
    def enterWhenClause(self, ctx:db2_parser.WhenClauseContext):
        pass

    # Exit a parse tree produced by db2_parser#whenClause.
    def exitWhenClause(self, ctx:db2_parser.WhenClauseContext):
        pass


    # Enter a parse tree produced by db2_parser#whenExpression.
    def enterWhenExpression(self, ctx:db2_parser.WhenExpressionContext):
        pass

    # Exit a parse tree produced by db2_parser#whenExpression.
    def exitWhenExpression(self, ctx:db2_parser.WhenExpressionContext):
        pass


    # Enter a parse tree produced by db2_parser#thenExpression.
    def enterThenExpression(self, ctx:db2_parser.ThenExpressionContext):
        pass

    # Exit a parse tree produced by db2_parser#thenExpression.
    def exitThenExpression(self, ctx:db2_parser.ThenExpressionContext):
        pass


    # Enter a parse tree produced by db2_parser#elseExpression.
    def enterElseExpression(self, ctx:db2_parser.ElseExpressionContext):
        pass

    # Exit a parse tree produced by db2_parser#elseExpression.
    def exitElseExpression(self, ctx:db2_parser.ElseExpressionContext):
        pass


    # Enter a parse tree produced by db2_parser#castExpression.
    def enterCastExpression(self, ctx:db2_parser.CastExpressionContext):
        pass

    # Exit a parse tree produced by db2_parser#castExpression.
    def exitCastExpression(self, ctx:db2_parser.CastExpressionContext):
        pass


    # Enter a parse tree produced by db2_parser#subquery.
    def enterSubquery(self, ctx:db2_parser.SubqueryContext):
        pass

    # Exit a parse tree produced by db2_parser#subquery.
    def exitSubquery(self, ctx:db2_parser.SubqueryContext):
        pass



del db2_parser