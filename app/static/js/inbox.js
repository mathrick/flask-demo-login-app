var InboxApp = angular.module('InboxApp', []);

InboxApp.controller('InboxCtrl', 
                    ['$scope', '$http', function InboxCtrl ($scope, $http) {
                        $http.get('/api/message/').success(function(data) {
                            $scope.messages = data;
                        });
                    }]);
