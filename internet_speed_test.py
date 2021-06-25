import speedtest

def main():
  conection = speedtest.Speedtest()

  downloadSpeed = conection.download()
  uploadSpeed = conection.upload()

  #ping
  conection.get_servers([]) 
  ping = conection.results.ping

  print("Your Ping is", ping)
  print("Your Download speed is", downloadSpeed)
  print("Your Upload speed is", uploadSpeed)

if __name__ == "__main__":
  main()