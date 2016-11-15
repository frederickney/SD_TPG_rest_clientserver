__author__ = 'Frederick NEY & Stephane Overlen'

import requests

import sys
import cmd


class Switch(object):
    value = None

    def __new__(class_, value):
        class_.value = value
        return True


def case(*args):
    return any((arg == Switch.value for arg in args))


def usage():
    print(sys.argv[0])
    print("\tWrite:")
    print("\t\twrite <text to write into file [between double cote]> > <file name [double cote needed if space(s)]>")
    print("\tRead:")
    print("\t\tread <file name [double cote needed if space(s)]>")
    print("\tHelp:\n\t\th or help")
    print("\tExiting:\n\t\tquit or exit")


def get_error(int, line, cmd):
    while Switch(int):
        if case(0):
            break
        if case(1):
            print("Missing arguments to: " + cmd)
            print("See usages using help")
            break
        if case(2):
            print("Unsupported operator: " + cmd + " " + line)
            print("See usages using help")
            break
        if case(3):
            print("Write: Missing operand '>' after text \"" + cmd + " " + line + "\"")
            print("See usages using help")
            break
        if case(4):
            print("Write: Missing file name after '>' \"" + cmd + " " + line + "\"")
            print("See usages using help")
            break
        print("Unsupported command: " + cmd + " " + line)
        print("See usages using help")
        break


class Main(cmd.Cmd):
    CMD = ['subscribe', 'unsubscribe', 'next_departure', 'list_stop_subscribed', 'list_all_stop', 'h', 'help', 'sign_in', 'sign_out', 'add_user', 'del_user', 'localisation']
    interpreter = interpreter.Cmd()

    def complete_read(self, text, line, begidx, endidx):
        if not text:
            return

    def complete_write(self, text, line, begidx, endidx):
        if not text:
            return

    def do_help(self, line):
        usage()


    def do_write(self, line):
        get_error(self.interpreter.analyse_cmd(line, 'write'), line, 'write')

    def do_read(self, line):
        get_error(self.interpreter.analyse_cmd(line, 'read'), line, 'read')

    def do_quit(self, line):
        exit(1)

    def do_exit(self, line):
        exit(1)

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    print("Use h or help to display command usage")
    cmd_interpreter = Main()
    cmd_interpreter.cmdloop()
