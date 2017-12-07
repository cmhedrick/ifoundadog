<form method="post" action="/lookup">
  <div class="form-group">
    <label for="inputLicense">Dog License</label>
    <input type="text" class="form-control" id="inputLicense" name="inputLicense" aria-describedby="inputLicenseHelp" placeholder="Dog License">
    <small id="inputLicenseHelp" class="form-text text-muted">Enter the Dog Liscense ID here.</small>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
<%rebase('templates/newbase.tpl', title='iFoundADog', addstyles=[], scripts=[]) %>
