def a (**kwargs):

    reslt=[{'syn_vlan_id': '0', 'syn_vlan_flag': '3', 'flowpassreason': 'NONE', 'trpy': 'TRPY_NONE', 'syn_seq': '0', 'ifwd_entry_aged': '0', 'fidx': '0',
    'src_port': '15008', 'ifwd_entries': '0', 'owner_ip': '172.16.45.2', 'dbg_vlan': '0', 'src_ip': ('172.16.47.2'),
    'cp_state': 'sh_owned', 'dbg_vlan_rev': '65535', 'redir_dst': 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', 'handle': '188218', 'relay': '0',
    'flow_protocol': 'TCP', 'nat_rcvd': '4', 'rcv_gre': '0', 'eal_dev_string': 'EAL_DEV_WAN', 'pkt_lb': '0', 'disc': '0', 'dst_port': '7850',
    'dst_ip': ('172.16.51.2'), 'ctx_id': '0'}, {'syn_vlan_id': '0', 'syn_vlan_flag': '3', 'flowpassreason': 'NONE', 'trpy': 'TRPY_NONE',
    'syn_seq': '0', 'ifwd_entry_aged': '0', 'fidx': '0', 'src_port': '15013', 'ifwd_entries': '0', 'owner_ip': ('172.16.45.2'), 
    'dbg_vlan': '0', 'src_ip': ('172.16.47.2'), 'cp_state': 'BYPASS', 'dbg_vlan_rev': '65535',
    'redir_dst': 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', 'handle': '188224', 'relay': '0', 'flow_protocol': 'TCP', 'nat_rcvd': '4', 'rcv_gre': '0',
    'eal_dev_string': 'EAL_DEV_WAN', 'pkt_lb': '0', 'disc': '0', 'dst_port': '7850', 'dst_ip': ('172.16.51.2'), 'ctx_id': '0'},
    {'syn_vlan_id': '0', 'syn_vlan_flag': '3', 'flowpassreason': 'NONE', 'trpy': 'TRPY_NONE', 'syn_seq': '4223282617', 'ifwd_entry_aged': '0',
    'fidx': '0', 'src_port': '7850', 'ifwd_entries': '0', 'owner_ip': ('172.16.45.2'), 'dbg_vlan': '0', 'src_ip': ('172.16.47.2'),
    'cp_state': 'BYPASS', 'dbg_vlan_rev': '65535', 'redir_dst': 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', 'handle': '188221', 'relay': '0', 
    'flow_protocol': 'TCP', 'nat_rcvd': '4', 'rcv_gre': '0', 'eal_dev_string': 'EAL_DEV_WAN', 'pkt_lb': '0', 'disc': '0', 'dst_port': '11970',
    'dst_ip': ('172.16.51.2'), 'ctx_id': '0'}, {'syn_vlan_id': '0', 'syn_vlan_flag': '3', 'flowpassreason': 'NONE', 'trpy': 'TRPY_FULL',
    'syn_seq': '0', 'ifwd_entry_aged': '0', 'fidx': '0', 'src_port': '15008', 'ifwd_entries': '0', 'owner_ip': ('172.16.45.2'), 
    'dbg_vlan': '0', 'src_ip': ('172.16.47.2'), 'cp_state': 'sh_owned', 'dbg_vlan_rev': '65535',
    'redir_dst': 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', 'handle': '188214', 'relay': '0', 
    'flow_protocol': 'TCP', 'nat_rcvd': '4', 'rcv_gre': '0', 'eal_dev_string': 'EAL_DEV_WAN', 'pkt_lb': '0', 'disc': '0', 
    'dst_port': '7850', 'dst_ip': ('172.16.51.2'), 'ctx_id': '0'}]
    count = 0
    for reslt_dict in reslt:
    		print "Inside 1st for loop"
                if (
                    str(reslt_dict['src_ip']) == str('172.16.47.2') and
                    str(reslt_dict['dst_ip']) == str('172.16.51.2') and
                    str(reslt_dict['src_port']) == str('15008') and
                    str(reslt_dict['dst_port']) == str('7850')
                  ):
                        print "Inside four tuple if block"
                        for key, vale in kwargs.items():
                            print "Inside 2nd for loop"
                            print key, vale, reslt_dict[key]
     			    if reslt_dict[key] == vale:
				print reslt_dict
                                break
                            else:
                                print("error")
                 
a(cp_state='sh_owned', trpy='TRPY_FULL')
