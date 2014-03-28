var InboxApp = angular.module('InboxApp', ['ngRoute', 'ui.bootstrap']);

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
                    ['$scope', '$http', '$routeParams', 
                     function InboxCtrl ($scope, $http, $params) {
                         $http.get('/api/users').success(function(data) {
                             $scope.users = data;
                             $scope.emails = Object.keys(data);
                         });

                         $scope.message = {};

                         $scope.send = function() {
                             $http.post('/api/message/', $scope.message)
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
