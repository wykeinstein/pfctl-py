import subprocess
import sys

def append_rule(anchor=None, rule= None):
    command = "pfctl -a " + anchor + " -sn"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    output = output.decode('utf-8')
    error = error.decode('utf-8')
    combined_rules = rule + output
    new_command = "pfctl -a " + anchor + " -Eef -"
    process = subprocess.Popen(new_command, stdin=subprocess.PIPE, shell=True)
    process.communicate(input=combined_rules.encode('utf-8'))


def just_append_rule(rule= None):
    command = "pfctl " + "-sn"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    output = output.decode('utf-8')
    error = error.decode('utf-8')
    combined_rules = rule + output
    new_command = "pfctl " + "-Eef -"
    process = subprocess.Popen(new_command, stdin=subprocess.PIPE, shell=True)
    process.communicate(input=combined_rules.encode('utf-8'))

args = sys.argv[1:]
if len(args) == 1:
    print (len(args))
    rule = args[0]
    if not rule.endswith('\n'):
        rule += '\n'
    just_append_rule(rule)
elif len(args) == 2:
    rule = args[1]
    anchor = args[0]
    if not rule.endswith('\n'):
        rule += '\n'
    append_rule(anchor=anchor, rule=rule)
else:
    print("Usage: python %s <anchor_name> <anchor_rule>")
    print("Usage: python %s \"<anchor_rule>\"")
    sys.exit()



