var InboxApp = angular.module('InboxApp', ['ngRoute', 'ngAnimate', 'ui.bootstrap']);

InboxApp.controller('InboxCtrl', 
                    ['$scope', '$http',
                     function InboxCtrl ($scope, $http) {
                         $http.get('/api/message/').success(function(data) {
                             $scope.messages = data;
                         });
                     }]);

InboxApp.controller('MessageCtrl', 
                    ['$scope', '$http', '$routeParams', 
                     function InboxCtrl ($scope, $http, $params) {
                         $http.get('/api/message/'+ $params.messageId).success(function(data) {
                             $scope.message = data;
                         });
                     }])

InboxApp.controller('ComposeCtrl', 
                    ['$scope', '$http', '$routeParams', '$location',
                     function InboxCtrl ($scope, $http, $params, $location) {
                         $http.get('/api/users').success(function(data) {
                             $scope.users = data;
                             $scope.emails = Object.keys(data);
                         });

                         $scope.message = { text: ""};

                         $scope.send = function() {
                             $http.post('/api/message/', $scope.message);
                             $location.path('/');
                         }
                     }])

InboxApp.config(['$routeProvider', function($route) {
    $route
        .when('/compose', {
            templateUrl: '/static/angular/compose.html',
            controller: 'ComposeCtrl'
        })
        .when('/:messageId', {
            templateUrl: '/static/angular/message.html',
            controller: 'MessageCtrl'
        })
        .otherwise({
            templateUrl: '/static/angular/inbox.html',
            controller: 'InboxCtrl'
        })
}])
