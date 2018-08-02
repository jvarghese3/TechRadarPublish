<html>
<header>
  <h1> Tech Radar </h1>
  <h4> Part 1 </h4>
<header>
<body>
    <p>This program takes messages from a Slack Channel and put them in AWS S3 as md5 hashes so they can be looked up and decoded later on. </p>
    <br>
      <p>This is the first part in a bigger project which will extract messages and user input, and search through them for useful information.</p>
    <br>
    <h5> What You Need </h5>
      1. SlackClient
  <br>
      2. Boto3
  <br>
      3. An S3 Bucket
  <br>
      4. A slack channel
  <br>
      5. Hashlib
  <br>
      6. Pip3
  <br>
      7. Python 3
    <br>
    <br>
    <h5> What it does </h5>
         * The first part of this program uses the Slack Converstions API to extract messages from the a Slack Channel.
      <p>* Slack's API accesses this channel by using a legacy token for the workspace.</p>
      <p>* It will also need the name of the channel or the last segment of the channel's URL.</p>
      <p>* You may need to allow permissions to the API for private channels if you choose to use an older API than the conversations API.</p>
      <p>* Then it converts those messages into hashes which takes the JSON returned from the Slack API and extracts the username and ts, which are constant, to create a hash in md5 format</p>
      <p>* After putting the hashes as the titles of json files in hte bucket, we can compare the titles to quickly remove duplicates</p>
      <p>* Every time the program runs, AWS will automatically replace duplicates with the newer version</p>
    <img src="Screen Shot 2018-08-01 at 2.16.12 PM">
    <br>
<p>In the future, the messages can be organized to see what is the most valuble technology for Intuit to invest in.</p>
  <br>
  <h5> Summary </h5>
  <p>Intuit Technology Futures’ Tech Radar project has a Slack Channel where Intuit employees go to discuss the latest technological advancements and to tell others what they’ve found. The channel contains a series of articles posted by members with comments from other contributors, with no particular order other than the chronological. The task was to extract these messages with their associated metadata, and place them into AWS S3 so they can be displayed, searched and processed in the future. This is the start of a much larger project, where we essentially create a smarter version of current search engines, which can efficiently rummage the internet to help you find the most relevant result related to the technologies Intuit is interested in. The main part of the first step is to look through the Tech Radar Slack channel and automatically find the most beneficial technologies for Intuit to invest in. This project proposes major benefit to Intuit’s future and is currently being developed in the Technology Future’s group.</p>
</body>
</html>
