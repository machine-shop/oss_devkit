# Open Source DevKit

Three tools to ease the life of Open Source developers:

- Command line Git module for working with GitHub, specifically GitHub PRs
- A bot
- An analytics dashboard (stalled PRs & discussions, time since last comment,
  etc.)

## Command Line
<b> ```git hub pr _```</b> <br />
&nbsp;&nbsp; Pulls down and checkout the branch of the pr. <br />

&nbsp;&nbsp; Parameters:  <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; num : integer
      The number of the pull request.
      
<b> ```git hub push```</b> <br />
&nbsp;&nbsp; Pushes changes back to a branch.

<b> ```git hub sync```</b> <br />
&nbsp;&nbsp; Updates and saves pull-requests in pull-requests.toml in the .git folder.

<b> ```git hub search _```</b> <br />
&nbsp;&nbsp; Pulls down and checkout the branch of the pr. <br />

&nbsp;&nbsp; Parameters:  <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; keyword : String
      Search string 
      
