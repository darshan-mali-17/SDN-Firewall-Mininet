from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

blocked_ip = "10.0.0.2"
mac_to_port = {}

def _handle_PacketIn(event):
    packet = event.parsed
    if not packet:
        return

    in_port = event.port
    mac_to_port[packet.src] = in_port

    ip_packet = packet.find('ipv4')

    if ip_packet:
        src_ip = str(ip_packet.srcip)

        if src_ip == blocked_ip:
            log.info("Blocking traffic from %s", src_ip)
            return

    if packet.dst in mac_to_port:
        out_port = mac_to_port[packet.dst]
    else:
        out_port = of.OFPP_FLOOD

    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=out_port))
    msg.in_port = in_port

    event.connection.send(msg)

def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)