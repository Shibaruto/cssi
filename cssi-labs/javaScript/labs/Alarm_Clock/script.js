// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

console.log("script is running...");
function Basic_Alarm(alarmMessage) {
  return alarmMessage;
}
console.log(Basic_Alarm("My alarm!"));
console.log();
function My_Alarm(time) { // it's < 7:30
  return "Hey, David, wake up! It's" + time;
}
console.log(My_Alarm("7:30"));
console.log();
function Mom_Alarm(time) { // it's < 8:00
  return "Hey, Mom, wake up! It's" + time;
}
console.log(Mom_Alarm("8:00"));
console.log();
function Family_Alarm(time) { // it's < 9:30
  return "Hey, cousin, wake up! It's" + time;
}
console.log(Family_Alarm("9:30"));
console.log();
function Important_Alarm(time) { // it's < 10:00
  return "WAKE UP, WAKE UP, WAKE UP!!" + time;
}
console.log(Important_Alarm("10:00"));
console.log();
function Snooze_Alarm(time) { // it's < 7:00
  return "The alarm for 7:00 has been changed to" + time;
}
console.log(Snooze_Alarm("7:30"));
console.log();
