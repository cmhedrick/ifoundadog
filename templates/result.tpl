<table class="table">
  <thead>
    <tr>
      <th scope="col">License ID</th>
      <th scope="col">Sex</th>
      <th scope="col">Spayed/Neutered</th>
      <th scope="col">Address</th>
      <th scope="col">Date Of Registration</th>
      <th scope="col">Length of Registration</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>{{result[4]}}</td>
      <td>{{result[5]}}</td>
      <td>{{result[6]}}</td>
      <td>{{result[1]}}</td>
      <td>{{result[2]}}</td>
      <td>{{result[3]}} Years</td>
    </tr>
  </tbody>
</table>
<%rebase('templates/newbase.tpl', title='Results', addstyles=[], scripts=[]) %>
