

__author__ = 'Frederick NEY & Stephane Overlen'


import functions.user as user
import cmd_loop as interpreter
import functions.tpg as tpg

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
    print("\tsubscribe:")
    print("\t\tsubscribe multiple or single stop")
    print("\tunsubscribe:")
    print("\t\tunsubscribe subscribe multiple or single stop")
    print("\tnext_departure:")
    print("\t\tlist next departure for single or multiple stop")
    print("\tstop_subscribed:")
    print("\t\tlist subscribed stops")
    print("\tall_stop:")
    print("\t\tlist all available stops")
    print("\tsign_in:")
    print("\t\tlog in into the server")
    print("\tsign_out:")
    print("\t\tlog out from the server")
    print("\tadd_user:")
    print("\t\tregister username")
    print("\tdel_user:")
    print("\t\tdel user and all of it information")
    print("\tlocalisation:")
    print("\t\tlist stop for a single or multiple position")
    print("\tHelp:\n\t\tdisplaying usages of commands")
    print("\tExiting:\n\t\tquit or exit (both will logout the user from the server)")


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
    CMD = [
        'subscribe',
        'unsubscribe',
        'next_departure',
        'stop_subscribed',
        'all_stop',
        'help',
        'sign_in',
        'add_user',
        'del_user',
        'localisation',
        'quit',
        'exit'
        ]
    interpreter_cmd = interpreter.Cmd()

    host = "localhost"
    port = 8000

    id = None
    hash = None

    def do_help(self, line):
        usage()

    def do_subscribe(self, line):
        if None == self.id or None == self.hash:
            print("please register first before deleting your user. see sign_in and add_user.")
            return
        if not None == line:
            args = line.split()
            if 0 < len(args):
                request = tpg.subscribe(self.id, self.hash, self.host, self.port, args)
                print(request['error'])
                return
        print("\thelp subscribe:\n\t\tlist of stop code <example: subscribe ACCM BLAN >")
        return

    def do_unsubscribe(self, line):
        if None == self.id or None == self.hash:
            print("please register first before deleting your user. see sign_in and add_user.")
            return
        if not None == line:
            args = line.split()
            if 0 < len(args):
                request = tpg.un_subscribe(self.id, self.hash, self.host, self.port, args)
                print(request['error'])
                return
        print("\thelp unsubscribe:\n\t\tlist of stop code <example : unsubscribe ACCM BLAN >")
        return

    def do_stop_subscribed(self, line):
        if None == self.id or None == self.hash:
            print("please register first before deleting your user. see sign_in and add_user.")
            return
        request = tpg.list_stop_subscribed(self.id, self.hash, self.host, self.port)
        if 'stop_subscribed' in request:
            for stops in request['stop_subscribed']:
                for stop in stops:
                    print("stop name : %s, stop code : %s" % (stop['stopName'], stop['stopCode']))
        else:
            print(request['error'])
        return


    def do_next_departure(self, line):
        if None == self.id or None == self.hash:
            print("please register first before deleting your user. see sign_in and add_user.")
            return
        if not None == line:
            args = line.split()
            if 0 < len(args):
                argv = []
                if '--handicapped' == args[0] and 2 < len(args):
                    for i in range(2, len(args)):
                        argv.append(args[1])
                    request = tpg.get_handicapped_next_dearture(self.id, self.hash, self.host, self.port, argv, 'stopCode')
                    if 'next_departure_handicaped' in request:
                        for stop in request['next_departure_handicaped']:
                            print("stop name : %s, stop code : %s" % (stop['stop']['stopName'], stop['stop']['stopCode']))
                            for departure in stop['departures']:
                                print('destination: %s, line number: %s, timestamp : %s' % (departure['line']['destinationName'], departure['line']['lineCode'], departure['timestamp']))
                    else:
                        print(request['error'])
                    return
                elif '--list' == args[0] and 1 < len(args):
                    for i in range(1, len(args)):
                        argv.append(args[i])
                    request = tpg.get_next_departure(self.id, self.hash, self.host, self.port, argv, 'stopCode')
                    if 'next_departure' in request:
                        if 'next_departure' in request:
                            for stop in request['next_departure']:
                                print("stop name : %s, stop code : %s" % (stop['stop']['stopName'], stop['stop']['stopCode']))
                                for departure in stop['departures']:
                                    if 'timestamp' in departure:
                                        print('destination: %s, line number: %s, timestamp : %s' % (departure['line']['destinationName'], departure['line']['lineCode'], departure['timestamp']))
                                    if 'waitingTime' in departure:
                                        print('destination: %s, line number: %s, waiting time : no more' % (departure['line']['destinationName'], departure['line']['lineCode']))
                    else:
                        print(request['error'])
                    return
        print("\thelp next_departure:\n\t\t<--handicapped optional> --list <example : --list ACCM BLAN>")
        return

    def do_all_stop(self, line):
        if None == self.id or None == self.hash:
            print("please register first before deleting your user. see sign_in and add_user.")
            return
        request = tpg.list_available_stop(self.id, self.hash, self.host, self.port)
        if 'stop_available' in request:
            for stops in request['stop_available']:
                for stop in stops:
                    print("stop name : %s, stop code : %s" % (stop['stopName'], stop['stopCode']))
        else:
            print(request['error'])
        return

    def do_sign_in(self, line):
        if not None == line:
            args = line.split()
            if 4 == len(args):
                username = None
                passwd = None
                if "-u" == args[0]:
                    username = args[1]
                elif "-u" == args[2]:
                    username = args[3]
                if "-p" == args[0]:
                    passwd = args[1]
                elif "-p" == args[2]:
                    passwd = args[3]
                if not None == username and not None == passwd:
                    request = user.sign_in(username, passwd, self.host, self.port)
                    if 'cookie_hepia_tpg' in request:
                        self.id = request['cookie_hepia_tpg']['id']
                        self.hash = request['cookie_hepia_tpg']['hash']
                    else:
                        print(request['error'])
                    return
        print("\thelp sign_in:\n\t\t-u username -p password")
        return

    def do_del_user(self, line):
        if None == self.id or None == self.hash:
            print("please register first before deleting your user. see sign_in and add_user.")
            return
        request = user.del_user(self.id, self.hash, self.host, self.port)
        print(request['error'])
        return

    def do_add_user(self, line):
        if not None == line:
            args = line.split()
            if 4 == len(args):
                username = None
                passwd = None
                if "-u" == args[0]:
                    username = args[1]
                elif "-u" == args[2]:
                    username = args[3]
                if "-p" == args[0]:
                    passwd = args[1]
                elif "-p" == args[2]:
                    passwd = args[3]
                if not None == username and not None == passwd:
                    request = user.add_user(username, passwd, self.host, self.port)
                    print(request['error'])
                    return
        print("\thelp add_user:\n\t\t-u username -p password")
        return

    def do_localisation(self, line):
        if None == self.id or None == self.hash:
            print("please register first before deleting your user. see sign_in and add_user.")
            return
        if not None == line:
            args = line.split()
            longitude = None
            latitude = None
            if 4 == len(args):
                if "--longitude" == args[0]:
                    longitude = args[1]
                elif "--longitude" == args[2]:
                    longitude = args[3]
                if "--latitude" == args[0]:
                    latitude = args[1]
                elif "--latitude" == args[2]:
                    latitude = args[3]
                if not None == longitude and not None == latitude:
                    request = tpg.get_stop_for_position(self.id, self.hash, longitude, latitude)
                    if 'locations' in request:
                        for stops in request['locations']:
                            for stop in stops:
                                print("stop name : %s, stop code : %s, distance %s" % (stop['stopName'], stop['stopCode'], stop['distance']))
                    else:
                        print(request['error'])
        print("\thelp localisation:\n\t\t--longitude longitude --latitude latitude")
        return

    def do_quit(self, line):
        if not None == self.id and not None == self.hash:
            request = user.sign_out(self.id, self.hash, self.host, self.port)
        exit(1)

    def do_exit(self, line):
        if not None == self.id and not None == self.hash:
            request = user.sign_out(self.id, self.hash, self.host, self.port)
        exit(1)


if __name__ == '__main__':
    print("Use h or help to display command usage")
    cmd_interpreter = Main()
    cmd_interpreter.cmdloop()
