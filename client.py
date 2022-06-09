import iperf3
import json
import datetime
import json.tool
import matplotlib.pyplot as plt

# client sends UPLOAD speed
# use -R reverse to get the DOWNLOAD speed (server sends and client receives)

client = iperf3.Client()
client.duration = 30
client.interval = 0.5
client.server_hostname = '192.168.1.70'
client.port = 5201
client.json_output = True
client.reverse = False  # False = upload, True = download
client.bidirectional = True


print('Connecting to: {0}:{1}'.format(client.server_hostname, client.port))
result = client.run()

if result.error:
    print(result.error)

else:
    print('')
    print('Test completed:')
    print('  started at         {0}'.format(result.time))
    print('  bytes transmitted  {0}'.format(result.sent_bytes))
    print('  retransmits        {0}'.format(result.retransmits))
    print('  avg cpu load       {0}%\n'.format(result.local_cpu_total))

    print('Average transmitted data in all sorts of networky formats:')
    print('  bits per second      (bps)   {0}'.format(result.sent_bps))
    print('  Kilobits per second  (kbps)  {0}'.format(result.sent_kbps))
    print('  Megabits per second  (Mbps)  {0}'.format(result.sent_Mbps))
    print('  KiloBytes per second (kB/s)  {0}'.format(result.sent_kB_s))
    print('  MegaBytes per second (MB/s)  {0}'.format(result.sent_MB_s))

if client.reverse:
    filename = "Download"+datetime.datetime.now().strftime('%H:%M:%S %Y-%m-%d') + ".json"

filename = "Upload"+datetime.datetime.now().strftime('%H:%M:%S %Y-%m-%d') + ".json"

file = open(filename, "w")
json.dump(result.json, file, indent=4, sort_keys=True)
# print(type(result.json)) ------ type is dict
file.close()

with open(filename) as json_data:
    data = json.load(json_data)
file.close()

print(data["intervals"][0]["streams"][0]["bits_per_second"])
n_intervals = len(data["intervals"])
print(n_intervals)

time = [0]
stream = [0]
plt.clf()
plt.title('Débit Upload')
plt.xlabel('Temps en secondes')
plt.ylabel('Débit en Mb/s')

for i in range(n_intervals):
    print(round(data["intervals"][i]["streams"]
                [0]["bits_per_second"] * 10e-6, 2))
    stream.append(round(data["intervals"][i]["streams"]
                  [0]["bits_per_second"] * 10e-6, 2))
    time.append(i+1)
    plt.plot(time, stream, color='blue')
    plt.draw()
    plt.pause(0.1)

plt.show()
# print(stream)
# print(time)
