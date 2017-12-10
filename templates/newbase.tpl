<!doctype html>
<html lang="en">
  <head>
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-51284230-3"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'UA-51284230-3');
    </script>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="Look up a lost dog's owner's address by their license.">
    <meta name="author" content="Christopher Hedrick of CFNoVA">
    <link rel="alternate" href="https://beta.ifoundadog.org/" hreflang="en" />
    <link rel="alternate" hreflang="x-default" href="https://beta.ifoundadog.org/" />
    <link rel="icon" href="../../../../favicon.ico">

    <title>{{title or 'Map App'}}</title>

    <!-- Bootstrap core CSS -->
    <link href="/static/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="/static/css/starter-template.css" rel="stylesheet">
    %for stylesheet in addstyles:
        @import url(/static/css/{{stylesheet}}.css);
    %end

  </head>

  <body>

    <nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
      <a class="navbar-brand" href="/">iFoundADog</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarsExampleDefault">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="http://www.codefornova.org/">Code for NoVA</a>
          </li>
        </ul>
        <form method="post" action="/lookup"  class="form-inline my-2 my-lg-0">
          <input class="form-control mr-sm-2" type="text" placeholder="Search" name="inputLicense" aria-label="Search">
          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
      </div>
    </nav>

    <main role="main" class="container">
      %include
    </main>
    <script src="/static/js/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script>window.jQuery || document.write('<script src="js/jquery.min.js"><\/script>')</script>
    <script src="/static/js/popper.min.js"></script>
    <script src="/static/js/bootstrap.min.js"></script>
    %for jsscript in addscripts:
        <script src="/static/js/{{jsscript}}.js"></script>
    %end
  </body>
</html>

