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

animateApp.controller('mainController', function($scope) {
    $scope.pageClass = 'email';
});

animateApp.controller('aboutController', function($scope) {
    $scope.pageClass = 'test';
});

console.log(gapi);