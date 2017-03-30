import time
import sys
global ISOTIMEFORMAT
ISOTIMEFORMAT='%X' # ISOTIMEFORMAT='%Y-%m-%d %X'

class Logger:
    level = 1
    def __init__(self, level):
        Dict = {"Error":3, "Warn":2,"Info":1,"Debug":0}
        self.level = Dict[level]
    def printError(self, string):
        local_level = 3
        if self.level <= local_level:
    	    timeStr = time.strftime( ISOTIMEFORMAT, time.localtime() )
    	    callerName = sys._getframe().f_back.f_code.co_name
    	    fileName = sys._getframe().f_back.f_code.co_filename
    	    lineNo = sys._getframe().f_back.f_lineno
    	    print "\033[1;31;48m[%s Error]\033[0mLine:%s(%s:%s)[%s]" % (timeStr,lineNo,callerName,fileName,string)
    def printWarn(self, string):
        local_level = 2
        if self.level < local_level:
    	    timeStr = time.strftime( ISOTIMEFORMAT, time.localtime() )	
    	    callerName = sys._getframe().f_back.f_code.co_name
    	    fileName = sys._getframe().f_back.f_code.co_filename
    	    lineNo = sys._getframe().f_back.f_lineno
    	    print "\033[1;34;48m[%s Warn]\033[0mLine:%s(%s:%s)[%s]" % (timeStr, lineNo,callerName,fileName,string)
    def printInfo(self, string):
        local_level = 1
        if self.level <= local_level:
    	    timeStr = time.strftime( ISOTIMEFORMAT, time.localtime() )
    	    callerName = sys._getframe().f_back.f_code.co_name
    	    fileName = sys._getframe().f_back.f_code.co_filename
    	    lineNo = sys._getframe().f_back.f_lineno
    	    print "\033[1;32;48m[%s Info]\033[0mLine:%s(%s:%s)[%s]" % (timeStr, lineNo,callerName,fileName,string)
    def printDebug(self, string):
        local_level = 0
        if self.level <= local_level:
    	    timeStr = time.strftime( ISOTIMEFORMAT, time.localtime() )
    	    callerName = sys._getframe().f_back.f_code.co_name
    	    fileName = sys._getframe().f_back.f_code.co_filename
    	    lineNo = sys._getframe().f_back.f_lineno
    	    print "\033[1;33;48m[%s Debug]\033[0mLine:%s(%s:%s)[%s]" % (timeStr, lineNo,callerName,fileName,string)

if __name__ == "__main__":
    logger = Logger("Info")
    logger.printInfo('''
        HELP: This module is used to print highlight logs:
        modify ISOTIMEFORMAT to control your time format, 
        hava a nice experience:)''')
