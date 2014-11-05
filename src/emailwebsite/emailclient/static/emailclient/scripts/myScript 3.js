var animateApp = angular.module('animateApp', ['ngRoute', 'ngAnimate', 'ui.bootstrap']);

animateApp.config(function($routeProvider) {
    $routeProvider

        .when('/', {
            templateUrl: 'views/email.html',
            controller: 'emailController'
        })
        .when('/send', {
            templateUrl: 'send',
            controller: 'sendController'
         })
        .when('/logout', {
            templateUrl: 'logout',
            controller: 'logoutController'
         })
        .when('/test', {
            templateUrl: 'test', 
            controller: 'testController'
        });

}); 
animateApp.controller('emailController', function($scope) {
    $scope.pageClass = 'email';
    $scope.currentSubject = 'GET TITLE FROM EMAIL';
    $scope.currentSender = 'Sender@example.com';
    $scope.currentMessage = 'Bacon ipsum dolor sit amet beef ribs landjaeger ribeye tongue, doner ball tip tenderloin pork belly strip steak meatball pancetta spare ribs kevin. Pork loin beef prosciutto frankfurter. Ham hock ball tip meatloaf, pork chop kevin jowl pork loin ground round pork belly chicken. Turkey meatloaf bacon tri-tip, landjaeger filet mignon ham hock pork belly bresaola doner boudin ground round. Shoulder tail spare ribs shankle. Andouille chicken ground round tenderloin, corned beef chuck brisket. Brisket sausage kevin tenderloin pork chop doner strip steak ribeye. Tongue sirloin shoulder, swine landjaeger capicola flank hamburger pastrami leberkas tri-tip spare ribs fatback. Strip steak sausage venison chuck doner drumstick, pork pork chop meatloaf meatball beef. Chuck boudin capicola shoulder drumstick ball tip meatloaf shankle. Turkey flank pork chop swine andouille hamburger cow drumstick tail.';
    $scope.currentTime = "22:24";
});


animateApp.controller('sendController', function($scope) {
    $scope.pageClass = 'send';
});


animateApp.controller('testController', function($scope) {
    $scope.pageClass = 'test';
});

animateApp.controller('logoutController', function($scope) {
    $scope.pageClass = 'logout';
});

animateApp.filter('range', function() {
  return function(input, total) {
    total = parseInt(total);
    for (var i=0; i<total; i++)
      input.push(i);
    return input;
  };
});

var dropdownController = function($scope){

    $scope.logout = function(){
      
    }
}

var mailController = function($scope){
    $scope.openMail = function(currentSubject, currentSender, currentMessage, currentTime){
        $scope.mailSubject = $scope.currentSubject;
        $scope.mailSender = $scope.currentSender;
        $scope.mailMessage = $scope.currentMessage;
        $scope.mailTime = $scope.currentTime;
    };
};


var replyController = function ($scope, $modal, $log) {

  $scope.items = ['Show more'];

  $scope.open = function (size, currentSubject, currentSender, currentMessage, currentTime) {

    var modalInstance = $modal.open({
      templateUrl: 'myModalContent.html',
      controller: ModalInstanceCtrl,
      size: size,
      resolve: {
        items: function () {
            return $scope.items;
        },
        currentSubject: function() {
            return currentSubject;
        },
        currentSender: function() {
            return currentSender;
        },
        currentMessage: function() {
            return currentMessage;
        },
        currentTime: function() {
            return currentTime;
        }
      }
    });
    
    modalInstance.result.then(function (selectedItem) {
      $scope.selected = selectedItem;
    }, function () {
      $log.info('Modal dismissed at: ' + new Date());
    });
  };
};

// Please note that $modalInstance represents a modal window (instance) dependency.
// It is not the same as the $modal service used above.

var ModalInstanceCtrl = function ($scope, $modalInstance, items, currentSubject, currentSender, currentMessage, currentTime) {

  $scope.items = items;
  $scope.currentSubject = currentSubject;
  $scope.currentSender = currentSender;
  $scope.currentMessage = currentMessage;
  $scope.currentTime = currentTime;


  $scope.selected = {
    // item: $scope.items[0]
    currentMessage: 'Detta kommer att ersättas'
  };

  $scope.ok = function () {
    $modalInstance.close($scope.selected.item);
  };

  $scope.cancel = function () {
    $modalInstance.dismiss('cancel');
  };
};

  var signInCallback = function (result) {
      if (result['error']) {
          //alert('An error happened:', result['error']);
      } 
      else if() {
        console.log("mums");
          var access_token = result['access_token'];
        gapi.auth.signOut();
        window.location = "/"
        console.log("yesss");
      }
  };