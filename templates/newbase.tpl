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
    <script type="text/javascript">
      var _bftn_options = {
        /*
         * Choose from 'countdown', 'glitch', 'money', 'stop', 'slow', 'without'.
         * Default is 'countdown'.
         */
        theme: 'glitch', // @type {string}

        /*
         * Or, if you want your own custom theme, specify its properties here.
         * Unspecified options will fall back to the default values.
         */

        /*
         * Choose from 'fp' for Free Press, 'dp' for Demand Progress or
         * 'fftf' for Fight for the Future. Omit this property to randomly split
         * form submissions between all organizations in the Battle for the Net
         * coalition.
         */
        org: 'fftf', // @type {string}

        /*
         * Specify a delay (in milliseconds) before showing the widget. Defaults to one
         * second.
         */
        delay: 1000, // @type {number}

        /*
         * Specify a date for the countdown theme. Defaults to November 23rd, 2017
         * (when the FCC is expected to announce a vote) if omitted. ISO-8601 dates are
         * UTC time, three-argument dates (with a zero-based month) are local time.
         */
        date: new Date(2017, 10, 23), // @type {Date}

        /*
         * Specify view cookie expiration. After initial view, modal will not be
         * displayed to a user again until after this cookie expires. Defaults to one
         * day.
         */
        viewCookieExpires: 1, // @type {number}

        /*
         * Specify action cookie expiration. After initiating a call or clicking a
         * donate link, modal will not be displayed to a user again until after this
         * cookie expires. Defaults to one week.
         */
        actionCookieExpires: 7, // @type {number}

        /*
         * If you show the modal on your homepage, you should let users close it to
         * access your site. However, if you launch a new tab to open the modal, closing
         * the modal just leaves the user staring at a blank page. Set this to true to
         * prevent closing the modal - the user can close the tab to dismiss it. Defaults
         * to false.
         */
        uncloseable: false, // @type {boolean}

        /*
         * Prevents the widget iframe from loading Google Analytics. Defaults to false.
         */
        disableGoogleAnalytics: false, // @type {boolean}

        /*
         * Always show the widget. Useful for testing.
         */
        always_show_widget: true // @type {boolean}
      };
    </script>
    <script async="" src="https://widget.battleforthenet.com/widget.js"></script>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="Look up a lost dog's owner's address by their license for Arlington, VA.">
    <meta name="author" content="Christopher Hedrick of CFNoVA">
    <link rel="alternate" href="https://beta.ifoundadog.org/" hreflang="en" />
    <link rel="alternate" hreflang="x-default" href="https://beta.ifoundadog.org/" />
    <link rel="icon" href="/static/images/icon.ico">
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
    <footer class="footer">
      <div class="container">
        <div class="row">
          <div class="col-12 col-md-8 white-text">Look up any dog in Arlington, VA using their dog license.</div>
        </div>
      </div>
    </footer>
    <script src="/static/js/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script>window.jQuery || document.write('<script src="js/jquery.min.js"><\/script>')</script>
    <script src="/static/js/popper.min.js"></script>
    <script src="/static/js/bootstrap.min.js"></script>
    %for jsscript in addscripts:
        <script src="/static/js/{{jsscript}}.js"></script>
    %end
  </body>
</html>

