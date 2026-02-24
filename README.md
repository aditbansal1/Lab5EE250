# Lab 5: Wireless Measurements

## Team Members
- Adit Bansal
- Aiden Fox

## Lab Question Answers

### Part 1: Signal Measurements

Question 1: What is dBm? What values are considered good and bad for WiFi signal strength?
dBm (decibel-milliwatts) is a logarithmic unit used to measure the power level of a radio signal. For WiFi, values closer to 0 are stronger; typically, -30 to -50 dBm is considered excellent, while values below -80 dBm are generally considered poor or unusable.

Question 2: Why do we need to check the OS? What is the difference between the commands for each OS?
Different operating systems use different command-line utilities to access hardware information[. Windows uses 'netsh', Linux uses 'iwconfig', and macOS uses 'networksetup' or 'wdutil', each returning data in different string formats and requiring different parsing logic.

Question 3: In your own words, what is subprocess.check_output doing? What does it return?
It runs a system command in the terminal from within the Python script and waits for it to complete. It returns the standard output of that command as a byte string, which we then decode for processing.

Question 4: In your own words, what is re.search doing? What does it return?
It searches a string for a specific pattern defined by a regular expression. It returns a match object if the pattern is found, which allows us to extract specific groups of text, such as the RSSI numerical value.

Question 5: In the Windows case, why do we need to convert the signal quality to dBm?
Windows reports signal strength as a percentage (quality) rather than a direct power level. We use the formula -100 + quality/2 to approximate the standard dBm value used for technical analysis and consistency across platforms.

Question 6: What is the standard deviation? Why is it useful to calculate it?
Standard deviation measures the amount of variation or "spread" in the signal strength samples. It is useful because it indicates the stability of the connection; a high standard deviation suggests an inconsistent signal prone to interference or environmental changes.

Question 7: What is a dataframe? Why is it useful to use a dataframe to store the data?
A DataFrame is a 2D labeled data structure provided by the Pandas library. It is useful for organizing complex datasets into rows and columns, making it easy to perform bulk calculations (like mean and std dev) and pass data directly to plotting libraries like Plotly.

Question 8: Why is it important to plot the error bars? What do they tell us?
Error bars visually represent the standard deviation of our measurements. They tell us the reliability and stability of the average signal strength at each location—wider bars mean more fluctuation, while short bars mean a very steady signal.

Question 9: What did you observe from the plot? How does the signal strength change as you move between locations? Why do you think signal strength is weaker in certain locations?
The bathroom showed the strongest signal strength around -41 dBm, while the hallway showed the weakest around -65 dBm. Signal strength generally decreased as distance from the router increased or when more walls were present. Weaker locations likely suffered from physical barriers like plumbing and thick walls that attenuate the signal.

---

### Part 2: Network Performance

Question 1: How does distance affect TCP and UDP throughput?
As distance increases, signal quality drops, leading to a reduction in throughput for both protocols. TCP throughput decreases as it slows down to ensure reliable delivery, while UDP throughput drops as more packets are lost in transit due to lack of signal integrity.

Question 2: At what distance does significant packet loss occur for UDP?
Based on the lab expectations, significant packet loss typically begins to appear at moderate distances (around 10m) and becomes severe at distances of 15m or more.

Question 3: Why does UDP experience more packet loss than TCP?
TCP is a connection-oriented protocol that adapts to weak signals by retransmitting lost packets. UDP is connectionless and does not retransmit, meaning any packet dropped due to distance or interference is permanently lost, leading to higher observed loss rates.

Question 4: What happens if we increase the UDP bandwidth (-b 100M)?
Increasing the requested bandwidth beyond what the physical link can handle causes the network buffers to overflow. This results in massive packet loss as the router or receiver is forced to drop the excess data it cannot physically process.

Question 5: Would performance be different on 5 GHz Wi-Fi vs. 2.4 GHz?
Yes. 5 GHz offers higher speeds but has a shorter range and weaker penetration through walls. 2.4 GHz provides better range and obstacle penetration but at significantly lower maximum throughput speeds.
