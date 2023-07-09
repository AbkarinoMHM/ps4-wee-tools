LINE_WIDTH = 70

# Helping stuff

def getTab(str):
	return '  _'+('_'*len(str))+'_\n'+('_/ '+str+' \_').ljust(LINE_WIDTH, '_')+'\n'

def showTable(data, pad=16):
	for key in data:
		print(' {} : {}'.format(key.ljust(pad,' '),data[key]))

def getMenu(menu, start=0):
	for n, text in enumerate(menu):
		print(' '+str(n+start)+': '+text)

STATUS = ''

def setStatus(v):
	global STATUS
	STATUS = v

def showStatus():
	global STATUS
	if STATUS:
		print(DIVIDER_DASH+STATUS)
		STATUS = ''

# Messages

DIVIDER = '_'*LINE_WIDTH+'\n'
DIVIDER_DASH = '-'*LINE_WIDTH+'\n'
DIVIDER_BOLD = '='*LINE_WIDTH+'\n'

TITLE = DIVIDER_BOLD+' PS4 ~WEE~ TOOLS v0.5 '+('by Andy_maN').rjust(LINE_WIDTH-23)+'\n'+DIVIDER_BOLD

TAB_FILE_LIST = getTab('Files list')
TAB_NOR_INFO = getTab('NOR dump info')
TAB_SYSCON_INFO = getTab('Syscon dump info')
TAB_COMPARE = getTab('Compare')
TAB_HELP = getTab('Help')
TAB_ACTIONS = getTab('Actions')
TAB_DOWNGRADE = getTab('Downgrade patterns')
TAB_MEMCLOCK = getTab('Memory clock')
TAB_SAMU_BOOT = getTab('SAMU boot')
TAB_SYSFLAGS = getTab('System flags')
TAB_LAST_SVNS = getTab('Last SNVS entries')
TAB_APATCH_SVNS = getTab('SNVS auto patching')
TAB_MPATCH_SVNS = getTab('SNVS manual patcher')
TAB_ENTROPY = getTab('Entropy statistics')
TAB_NOR_FLAGS = getTab('NOR flags')

MENU_NOR_ACTIONS = [
	'Select another file',
	'Flags (UART, RNG, Memtest, etc)',
	'Memory clocking (GDDR5)',
	'SAMU boot flag',
	'Downgrade - CoreOS slot switching',
	'Entropy check',
	'Exit'
]

MENU_SC_ACTIONS = [
	'Select another file',
	'Toggle Debug',
	'Show active SNVS block',
	'Auto SNVS patch',
	'Manual SNVS patch',
	'Exit'
]

MENU_PATCHES = [
	'Method A - last 08-0B will be cleaned (4 records)',
	'Method B - last 08-0B and below will be cleaned ({} records)',
	'Method C - last 08-0B will be replaced with previous',
	'Method D - fix counters (f.e. after method C)',
]

MSG_NO_INFO = '- No info -'
MSG_OFF = 'Off'
MSG_ON = 'On'
MSG_WAIT = ' Please wait...'
MSG_YES = 'Yes'
MSG_NO = 'No'
MSG_PROBABLY = 'Probably'
MSG_NOT_SURE = 'not sure'
MSG_SET_TO = ' {} was set to [{}]'

MSG_NIY = ' Function is not implemented yet'
MSG_CLEAN_FLAGS = ' Clean all system flags'
MSG_UNK_FILE_TYPE = ' Unknown file type'
MSG_UART = ' UART is set to '
MSG_DEBUG = ' Sycon debug is set to '

MSG_DIFF_SLOT_VALUES = ' Values in slots are different!'
MSG_SYSFLAGS_CLEAN = ' Sys flags were cleared. Tip: turn on UART'
MSG_SAMU_UPD = ' SAMU flag was set to '
MSG_DOWNGRADE_UPD = ' Downgrade was set to: '
MSG_SNVS_ENTRIES = '{} records found at 0x{:5X}'
MSG_LAST_DATA = ' Last {} records of {}: '

MSG_PATCH_CANCELED = ' Patch was canceled'
MSG_PATCH_SUCCESS = ' Successfully removed {} entries'
MSG_PATCH_SAVED = ' Patch was saved to {}'
MSG_UNPATCHABLE = ' Can\'t procced. Last SNVS record #{} counter [0x{:02X}] type [0x{:02X}]'
MSG_PATCH_INDEXES = ' Last 08-0B at 0x{:04X} | Previous at 0x{:04X}\n'

MSG_MPATCH_INPUT = DIVIDER + ' How many records to clean (from end): '
MSG_CHOICE = DIVIDER + ' Make choice: '
MSG_BACK = DIVIDER + ' Press [ENTER] to go back'
MSG_MEMCLOCK_INPUT = DIVIDER + ' Setup frequency [400 - 2000] / [0 set default (0xFF)] MHz '
MSG_SAMU_INPUT = DIVIDER + ' Setup SAMU [0 - 255] / [default is 255 (0xFF)] '

MSG_INCORRECT_SIZE	= ' {} - incorrect dump size!'
MSG_FILE_NOT_EXISTS	= ' File {} doesn\'t exist!'
MSG_ERROR_INPUT		= ' Incorrect input'
MSG_ERROR_DEF_VAL	= ' Setting default values'
MSG_ERROR_CHOICE	= ' Invalid choice'
MSG_OUT_OF_RANGE	= ' Value is out of range!'
MSG_FILES_MATCH		= ' Files are equal'
MSG_FILES_MISMATCH	= ' Files mismatch'

MSG_CONFIRM = DIVIDER + ' Input [y] to continue: '
MSG_CURRENT = ' Current: '
MSG_GO_BACK = ' Go back'

MSG_OVERCLOCKING = getTab('Warning')+\
'\n'\
' Dangerous operation! \n'\
' Most GDDR5 runs at 6000-8000 MHz. GDDR5 is quad pumped [x4]\n'\
' GDDR5 at 8000 MHz technically runs at 2000 MHz\n'\
' If you have problems, lower frequency to 1000 MHz\n'\
'\n'\
' Effective GDDR5 clock is 1350 MHz\n'\
' The frequency is selected experimentally\n'\
' - Too high value can lead to LOADBIOS -8 or DCT [*] error\n'\
' - Too low value leads to AMDINIT error \n'

MSG_PATCHES = getTab('Warning')+\
'\n'\
' Be careful: All patches are applied immediatly to file! \n'\
' Will switch value between available values for chosen option \n'

MSG_DOWNGRADE = getTab('Warning')+\
'\n'\
' Dangerous operation! \n'\
' Make sure you have backup of stock NOR dump.\n'\
' Syscon patching required - otherwise you\'ll get "loadbios" error.\n'\
' Console will not boot normally.\n'

MSG_INFO_SC_MPATCH = getTab('Manual patch instructions')+\
'\n'\
' Every record is 16 bytes length. First byte is always "A5"\n'\
' The second byte is record "type" usualy in range [08-2B]\n'\
' Firmware update takes 4 records with types "08-0B"\n'\
' To cancel last fw update we need to clean these 4 records (fill 0xFF)\n'\
' If there are "0C-0F","20-23" types after "08-0B" patch is impossible\n'\
' backup slot is already erased, you\'ll got checkUpdVersion error\n'

MSG_HELP = getTab('Help')+\
'\n'\
' Usage: ps4-wee-tools <file1> <file2> ... \n'\
'  - One <file>: auto detects file type and loads appropriate tool\n'\
'  - Multi <files>: compare mode (with MD5 info)\n'\
'  - help: show this help screen\n'\
'\n'\
' File selection works only for *.bin files within app\'s directory\n'\
'\n'\
' Home: https://github.com/andy-man/ps4-wee-tools'
