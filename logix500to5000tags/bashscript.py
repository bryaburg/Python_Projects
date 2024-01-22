"""Quick Bash script for ouput
for x in $(seq 1 $(wc -l K45791_01_17_{slot}0{addr}slot}4{addr}Comments.CSV | cut -f1 -d" "))
do
    line=$(cat K45791_01_17_{slot}0{addr}slot}4{addr}Comments.CSV | head -n +"$x" | tail -n 1)
    iostr=$(echo "$line" | cut -f1 -d,)
    desc=$(echo "$line" | cut -f4 -d,)
    ioaddr=$(echo "$iostr" | cut -f1 -d":")
    ioslot=$(echo "$iostr" | cut -f{slot} {addr}d":" | cut -f1 -d"/")
    ioterminal=$(echo "$iostr" | cut -f{slot} {addr}d":" | cut -f{slot} {addr}d"/")
    printf "COMMENT,,Local:%s:%s,%s,,\"Local:%s:%s.DATA.%s\"\n" "$ioslot" "$ioaddr" "$desc" "$ioslot" "$ioaddr" "$ioterminal"
done

TAG,,Local:{slot}:{addr},"","AB:1756_D{addr}:{addr}:0","","(ExternalAccess := Read/Write)"
COMMENT,,Local:{slot}:{addr},"{description}",,"Local:{slot}:{addr}.DATA.{terminal}"
COMMENT,,Local:{slot}:{addr},"{description}",,"Local:{slot}:{addr}.DATA.{terminal}"
COMMENT,,Local:{slot}:{addr},"{description}",,"Local:{slot}:{addr}.DATA.{terminal}"
COMMENT,,Local:{slot}:{addr},"{description}",,"Local:{slot}:{addr}.DATA.{terminal}"
COMMENT,,Local:{slot}:{addr},"{description}",,"Local:{slot}:{addr}.DATA.{terminal}"
COMMENT,,Local:{slot}:{addr},"{description}",,"Local:{slot}:{addr}.DATA.{terminal}"
COMMENT,,Local:{slot}:{addr},"{description}",,"Local:{slot}:{addr}.DATA.{terminal}"
COMMENT,,Local:{slot}:{addr},"{description}",,"Local:{slot}:{addr}.DATA.{terminal}"
COMMENT,,Local:{slot}:{addr},"{description}",,"Local:{slot}:{addr}.DATA.{terminal}"
COMMENT,,Local:{slot}:{addr},"{description}",,"Local:{slot}:{addr}.DATA.{terminal}"
COMMENT,,Local:{slot}:{addr},"{description}",,"Local:{slot}:{addr}.DATA.{terminal}"
COMMENT,,Local:{slot}:{addr},"{description}",,"Local:{slot}:{addr}.DATA.{terminal}"
"""

