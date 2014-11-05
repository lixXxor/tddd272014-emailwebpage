var animateApp = angular.module('animateApp', ['ngRoute', 'ngAnimate']);

animateApp.config(function($routeProvider) {
    $routeProvider

        .when('/', {
            templateUrl: 'views/email.html',
            controller: 'mainController'
        })
        .when('/test', {
            templateUrl: 'views/test.html',
            controller: 'aboutController'

        });

});

animateApp.controller('emailController', function($scope) {
    $scope.pageClass = 'email';
});

animateApp.controller('sendController', function($scope) {
    $scope.pageClass = 'send';
});

function signOut(){
    gapi.auth.signOut();
    window.location.hash = "logout";
};