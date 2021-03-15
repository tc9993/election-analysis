<h1>Election Analysis</h1>

<h2>Overview</h2>

<h3>Purpose</h3>
<p>
The Colorado Board of Elections is conducting an election audit for a congressional district's election.  They would like the following information tabulated:
<ul>
  <li>Total Number of Votes Cast</li>
  <li>Full list of candidates receiving votes, how many each, and the percentage of the total vote</li>
  <li>The winner of the election</li>
  <li>Full list of counties, how many voters participated in each, and what percentage of total voters that county accounts for</li>
  <li>The county with the largest voter turnout</li>
</ul>
</p>

<h3>Resources</h3>

<ul>
  <li>Data Source: \Resources\election_results.csv</li>
  <li>Software: Python 3.7.6, Visual Studio Code</li>
</ul>

<h2>Results</h2>

<h3>Election-Audit Results</h3>

<ul>
  <li>How many votes were cast in this congressional election?
  <ul>
    <li>There were a total of 369,711 votes cast</li>
    </ul>
  </li>
  <li>Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.<br>
    <table>
      <tr>
      <th>County Name</th>
      <th>Total Votes Cast</th>
      <th>Percent of Total Votes</th>
      <tr>
        <td>Jefferson</td>
        <td>38,855</td>
        <td>10.5%</td>
      </tr>
      <tr>
        <td>Denver</td>
        <td>306,055</td>
        <td>82.8%</td>
      </tr>
      <tr>
        <td>Arapahoe</td>
        <td>24,801</td>
        <td>6.7%</td>
      </tr>
    </table>
  </li>
    <li>Which county had the largest number of votes?
    <ul>
      <li>Denver county had the largest number of votes cast both in total and as a percentage.</li>
    </ul>
  </li>
    <li>Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
    <table>
      <tr>
        <th>Candidate</th>
        <th>Total Votes Received</th>
        <th>Percentage of Votes Received</th>
      </tr>
      <tr>
        <td>Charles Casper Stockham</td>
        <td>85,213</td>
        <td>23.0%</td>
      </tr>
      <tr>
        <td>Diana DeGette</td>
        <td>272,892</td>
        <td>73.8%</td>
      </tr>
      <tr>
        <td>Raymon Anthony Doane</td>
        <td>11,606</td>
        <td>3.1%</td>
      </tr>
      </table>
  </li>
    <li>Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
    <ul>
      <li>Diana DeGette won the election with 272,892 votes, or 73.8%.</li>
    </ul>
  </li>
  
  <h2>Election Audit Summary</h2>
  
  <h3>Script Reusability</h3>
  <p>
  The script contained in this repository can be used to tabulate the results of any election with minimal, if any, modifications to the script required.  The script itself can be used for other elections because it dynamically finds the different county and candidate names and files them away without needing the values in advance.  A few requirements would need to be met in order for it to run for <i>any election</i>:
  <ol>
    <li>An acceptable file name for the data set would need to be "election_results.csv" and be placed in the "Resources" directory.</li>
    <li>It must be acceptable for the results to be printed out to a text file entitled "election_analysis.txt" in the "Analysis" directory.</li>
  </ol>
  </p>
  <p>
  If changes are needed to either of the two items above, modifications would be needed as follows:
  <ul>
    <li>Regarding Item 1 above: Changing line 6 of the code to reflect either the correct file path <i>or</i> file name would be required to ensure the correct data set is being used to tabulate results.</li>
    <li>Regarding Item 2 above: Changing lines 8 of the code to reflect the desired output directory <i>or</i> output file name would be required.</li>
  </ul>
  </p>
