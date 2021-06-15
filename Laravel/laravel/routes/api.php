<?php

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
 */
Route::group(['middleware' => 'api'], function () {
    Route::post('login', [Controller::class, 'login']);
    Route::post('register', [Controller::class, 'register']);

});
Route::group(['middleware' => ['api', 'auth:sanctum']], function () {
    Route::get('check', [Controller::class, 'checkIfLogged']);
});
Route::middleware('auth:api')->get('/user', function (Request $request) {
    return $request->user();
});
