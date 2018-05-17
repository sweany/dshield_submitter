# DSHIELD Submitter

Submit iptables logs to the DSHIELD project; see https://dshield.org/specs.html

The iptables statements I use at the end of my input chain are:

```
iptables -A INPUT -m tcp -p tcp -j LOG --log-prefix "type=ingress "
iptables -A INPUT -m udp -p udp -j LOG --log-prefix "type=ingress "
```


