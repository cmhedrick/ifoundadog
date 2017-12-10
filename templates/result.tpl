<table class="table table-responsive">
  <thead>
    <tr>
      <th scope="col">License ID</th>
      <th scope="col">Sex</th>
      <th scope="col">Spayed/Neutered</th>
      <th scope="col">Address</th>
      <th scope="col">Date Of Registration</th>
      <th scope="col">Length of Registration</th>
      <th scope="col">Expired</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="licenseID">{{result[4]}}</td>
      <td id="sex">{{result[5]}}</td>
      <td id="neutered">{{result[6]}}</td>
      <td id="address">{{result[1]}}</td>
      <td id="dateOfReg">{{result[2]}}</td>
      <td id="lengthOfReg">{{result[3]}} Years</td>
      <td id="expired">N/A</td>
    </tr>
  </tbody>
</table>
<%rebase('templates/newbase.tpl', title='Results', addstyles=[], addscripts=['date-helper']) %>
