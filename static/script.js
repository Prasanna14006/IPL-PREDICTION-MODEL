const teams = ["CSK", "MI", "RCB", "KKR", "SRH", "DC", "RR", "PBKS", "LSG", "GT"];
const venues = ["M. A. Chidambaram Stadium, Chennai", "Wankhede Stadium, Mumbai", "M. Chinnaswamy Stadium, Bangalore", "Eden Gardens, Kolkata", "Sawai Mansingh Stadium, Jaipur", "Arun Jaitley Stadium, Delhi", "PCA Stadium, Mohali", "Rajiv Gandhi Intl. Stadium, Hyderabad", "Narendra Modi Stadium, Ahmedabad", "BRSABV Ekana Stadium, Lucknow"];

function populateDropdown(selectElement, options, placeholder) {
  selectElement.innerHTML = `<option disabled selected>${placeholder}</option>`;
  options.forEach(option => {
    const opt = document.createElement("option");
    opt.value = option;
    opt.textContent = option;
    selectElement.appendChild(opt);
  });
}
  
document.addEventListener("DOMContentLoaded", () => {
  const team1Select = document.getElementById("team1");
  const team2Select = document.getElementById("team2");
  const venueSelect = document.getElementById("venue");
  const tossWinnerSelect = document.getElementById("toss_winner");
  const tossDecisionSelect = document.getElementById("toss_decision");

  populateDropdown(team1Select, teams, "Select Team 1");
  populateDropdown(team2Select, teams, "Select Team 2");
  populateDropdown(venueSelect, venues, "Select Venue");
  populateDropdown(tossDecisionSelect, ["bat", "field"], "Select Decision");

  team1Select.addEventListener("change", () => {
    const team1 = team1Select.value;
    const filteredTeams = teams.filter(t => t !== team1);
    populateDropdown(team2Select, filteredTeams, "Select Team 2");
    team2Select.disabled = false;

    // Clear toss winner
    tossWinnerSelect.innerHTML = `<option disabled selected>Select Toss Winner</option>`;
    tossWinnerSelect.disabled = true;
  });

  team2Select.addEventListener("change", () => {
    const team1 = team1Select.value;
    const team2 = team2Select.value;
    if (team1 && team2) {
      populateDropdown(tossWinnerSelect, [team1, team2], "Select Toss Winner");
      tossWinnerSelect.disabled = false;
    }
  });
});
