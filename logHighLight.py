import time
import sys
global ISOTIMEFORMAT
ISOTIMEFORMAT='%X' # ISOTIMEFORMAT='%Y-%m-%d %X'

def printError(string):
	timeStr = time.strftime( ISOTIMEFORMAT, time.localtime() )
	callerName = sys._getframe().f_back.f_code.co_name
	fileName = sys._getframe().f_back.f_code.co_filename
	lineNo = sys._getframe().f_back.f_lineno
	print "\033[1;31;48m[%s Error]\033[0mLine:%s(%s:%s)[%s]" % (timeStr,lineNo,callerName,fileName,string)

def printInfo(string):
	timeStr = time.strftime( ISOTIMEFORMAT, time.localtime() )
	callerName = sys._getframe().f_back.f_code.co_name
	fileName = sys._getframe().f_back.f_code.co_filename
	lineNo = sys._getframe().f_back.f_lineno
	print "\033[1;32;48m[%s Info]\033[0mLine:%s(%s:%s)[%s]" % (timeStr, lineNo,callerName,fileName,string)

def printDebug(string):
	timeStr = time.strftime( ISOTIMEFORMAT, time.localtime() )
	callerName = sys._getframe().f_back.f_code.co_name
	fileName = sys._getframe().f_back.f_code.co_filename
	lineNo = sys._getframe().f_back.f_lineno
	print "\033[1;33;48m[%s Debug]\033[0mLine:%s(%s:%s)[%s]" % (timeStr, lineNo,callerName,fileName,string)

def printWarn(string):
	timeStr = time.strftime( ISOTIMEFORMAT, time.localtime() )	
	callerName = sys._getframe().f_back.f_code.co_name
	fileName = sys._getframe().f_back.f_code.co_filename
	lineNo = sys._getframe().f_back.f_lineno
	print "\033[1;34;48m[%s Warn]\033[0mLine:%s(%s:%s)[%s]" % (timeStr, lineNo,callerName,fileName,string)

if __name__ == "__main__":
	printInfo('''
	HELP: This module is used to print highlight logs:
	modify ISOTIMEFORMAT to control your time format, 
	hava a nice experience:)''')
