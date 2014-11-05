var animateApp = angular.module('animateApp', ['ngRoute', 'ngAnimate', 'ui.bootstrap', 'ngSanitize']);

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
    $scope.emailList = emailArray;
});


// animateApp.controller('sendController', function($scope) {
//     $scope.pageClass = 'send';
// });


// animateApp.controller('testController', function($scope) {
//     $scope.pageClass = 'test';
// });

animateApp.controller('logoutController', function($scope) {
    $scope.pageClass = 'logout';
});

var dropdownController = function($scope){
}

var mailController = function($scope){
    $scope.openMail = function(currentSubject, currentSender, html, body, currentTime){
        $scope.mailSubject = currentSubject;
        $scope.mailSender = currentSender;
        if(html != null)
            $scope.mailMessage = html;  
        else
            $scope.mailMessage = body;
        $scope.mailTime = currentTime;
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

  $scope.ok = function (yourSubject, yourSender, yourMessage) {
    console.log(token);
    
    $.get("sendMail", {to: yourSender, 
            subject: yourSubject, 
            message: yourMessage, 
            access_token: token.access_token}, function (arg) {
            console.log(arg);
    });
    $modalInstance.close($scope.selected.item);
  };

  $scope.cancel = function () {
    $modalInstance.dismiss('cancel');
  };
};
