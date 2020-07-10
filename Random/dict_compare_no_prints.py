def redirreq_table_contents(src_ip, dst_ip, src_port, dst_port, **kwargs):

    result = [{u'cp_state': u'BYPASS',
              u'ctx_id': u'0',
              u'dbg_vlan': u'0',
              u'dbg_vlan_rev': u'65535',
              u'disc': u'0',
              u'dst_ip': u'172.16.221.2',
              u'dst_port': u'13375',
              u'eal_dev_string': u'EAL_DEV_WAN',
              u'fidx': u'0',
              u'flow_protocol': u'TCP',
              u'flowpassreason': u'NONE',
              u'handle': u'2714203',
              u'ifwd_entries': u'0',
              u'ifwd_entry_aged': u'0',
              u'nat_rcvd': u'4',
              u'owner_ip': u'172.16.211.2',
              u'pkt_lb': u'0',
              u'rcv_gre': u'0',
              u'redir_dst': u'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff',
              u'relay': u'0',
              u'src_ip': u'172.16.217.4',
              u'src_port': u'7850',
              u'syn_seq': u'0',
              u'syn_vlan_flag': u'3',
              u'syn_vlan_id': u'0',
              u'trpy': u'TRPY_NONE'},
              {u'cp_state': u'BYPASS',
              u'ctx_id': u'0',
              u'dbg_vlan': u'0',
              u'dbg_vlan_rev': u'65535',
              u'disc': u'0',
              u'dst_ip': '172.16.221.2',
              u'dst_port': u'12802',
              u'eal_dev_string': u'EAL_DEV_WAN',
              u'fidx': u'0',
              u'flow_protocol': u'TCP',
              u'flowpassreason': u'NONE',
              u'handle': u'2715318',
              u'ifwd_entries': u'0',
              u'ifwd_entry_aged': u'0',
              u'nat_rcvd': u'4',
              u'owner_ip': u'172.16.211.2',
              u'pkt_lb': u'0',
              u'rcv_gre': u'0',
              u'redir_dst': u'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff',
              u'relay': u'0',
              u'src_ip': u'172.16.217.2',
              u'src_port': u'7850',
              u'syn_seq': u'0',
              u'syn_vlan_flag': u'3',
              u'syn_vlan_id': u'0',
              u'trpy': u'TRPY_NONE'}]

    if result == []:
        print "List is 0"

    found = 0
    for result_dict in result:
        if (str(result_dict['src_ip']) == str(src_ip) and \
            str(result_dict['dst_ip']) == str(dst_ip) and \
            str(result_dict['src_port']) == str(src_port) and \
            str(result_dict['dst_port']) == str(dst_port)):
                for key, value in kwargs.items():
                    print key, value, result_dict[key]
                    if result_dict[key] == value :
                        found = 1
                    else :
                        found = 0
                if found:
	            print "Exact match with kwargs"
                    break
    if not found:
        print "Match not found"

new_dict = {'cp_state': 'BYPASS', 'flow_protocol': 'TCP', 'trpy': 'TRPY_NONE' }
redirreq_table_contents(src_ip = '172.16.217.4',
                        dst_ip = '172.16.221.2',
                        src_port = '7850',
                        dst_port = '13375',
                        #cp_state = "BYPASS",
                        #flow_protocol = "TCP",
                        **new_dict)
