/**
 * Created by gamolyavlad on 3/7/16.
 */
var app = angular.module('app',[])
app.controller('mainCtrl',['$scope','$http',function ($scope,$http){
    $scope.name = 'Vlad'
    $scope.sendText = function (){
        $http({
            'method':'GET',
            'url':'/searchText/'+$scope.searchText+"/"
        }).then(function successCallback(data){
            console.log(data)
        },function errorCallback(data){
            console.log(data)
        })
    }
}])
console.log('ok')