var InboxApp = angular.module('InboxApp', ['ngRoute']);

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

InboxApp.config(['$routeProvider', function($route) {
    $route
        .when('/message/:messageId', {
            templateUrl: '/static/angular/message.html',
            controller: 'MessageCtrl'
        })
        .when('/inbox/', {
            templateUrl: '/static/angular/inbox.html',
            controller: 'InboxCtrl'
        })
        .otherwise({
            templateUrl: '/static/angular/inbox.html',
            controller: 'InboxCtrl'
        })
}])
