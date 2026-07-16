SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2026-07-15
Duration: 11 minutes
============================================================

## Zoom Recording Transcript

**Jim Porell** 01:12 Hey, welcome to the non-meeting.
**Greg Shriver** 01:15 I hate you.
How are you?
**Jim Porell** 01:18 Good. I just saw that neither Rudiger or Antoine are joining.
**Greg Shriver** 01:23 Right. Yeah.
Yeah, I took a look at, were you on last week? I was on vacation.
**Jim Porell** 01:32 I've been out for a month. I had another surgery, so.
**Greg Shriver** 01:36 Oh, I'm sorry to hear that.
**Jim Porell** 01:38 Yeah, no, it's, believe it or not, it's at the VM workshop.
And I popped my Achilles, moving the mainframe to the truck.
**Greg Shriver** 01:48 Oh, no way.
**Jim Porell** 01:50 Yes.
**Greg Shriver** 01:51 Oh.
**Jim Porell** 01:51 Like, what a disaster. We moved it 20 feet to the door.
They had a pallet fork that was too small or too large for the size of the box, so they could only get one fork in it. So two people were leaning on the other fork that tilted up. I was pushing it on one side. We got to the door.
Truck driver moved the truck close to the door and then on a second push.
**Greg Shriver** 02:14 Pop.
**Jim Porell** 02:14 So surgery and I'm recovering from that. I'm sitting here with ice on my leg right now.
**Greg Shriver** 02:20 Oh, man. Oh, I'm sorry, dude.
**Jim Porell** 02:23 It's pretty, it's pretty freaking funny though when you think about it.
**Greg Shriver** 02:27 Well, it's funny, but it's not.
**Jim Porell** 02:29 No, I know, I know. It's kind of wrecked the summer, but,
**Greg Shriver** 02:32 Well, yeah, that's gonna be limiting, for sure.
**Jim Porell** 02:36 Yeah, but I can walk.
I can walk. I have to walk with crutches, but I can walk on it without pain. I'm in no pain. That's good. Surgery is 33 minutes, really fast. In fact, I went in on a Wednesday.
talked to the doctor and he goes, "I could do the surgery tomorrow, but I'm on the float in the Knicks parade. I'm their team doctor." So I was in very good hands.
**Greg Shriver** 03:00 Yeah, it sounds like… sounds like you had somebody that knew what they were doing, yeah.
**Jim Porell** 03:03 Yeah, definitely. Definitely. Yeah.
**Greg Shriver** 03:06 And you'll be back on the basketball court soon.
**Jim Porell** 03:08 Oh, yeah, definitely. I'll be better. I can jump higher, faster.
**Greg Shriver** 03:11 Yes!
**Jim Porell** 03:12 Really now.
**Greg Shriver** 03:12 Right, exactly.
**Jim Porell** 03:13 a dollar man, yeah.
**Greg Shriver** 03:14 Be the bionic man. Yeah, exactly. Yeah. You, you have that, that, that, that.
Oh.
That sound effect when you, like, run and stuff?
**Jim Porell** 03:23 Ba-na-na-na-na-na-na-na-na.
**Greg Shriver** 03:26 The same.
**Jim Porell** 03:27 I'm gonna have to tap that in.
**Greg Shriver** 03:29 That's awesome.
Yeah, so I don't really have anything today. I… so I don't know if you took a look, but… In the Semantic Convention, the Semantic Convention's mainframe repository.
Which is a clone of the Gen AI repository, which is…
**Jim Porell** 03:47 Right.
**Greg Shriver** 03:48 the first penguin of the Federated Semantic Conventions.
So there's a PR in there.
There's a PR in there, to… to… get the HMC stuff in there, that… that,
**Jim Porell** 04:04 Oh, okay.
**Greg Shriver** 04:04 That Rudiger put together. I think they reviewed that last week, that was on the agenda, but I don't know how far they got. I started looking at it, and… you know, there's a lot of stuff in there that I, quite honestly, don't understand, because a lot of this stuff is kind of new.
So maybe next week, we can ask Rutiger and… Others to explain what's in there.
Okay.
So, I did open an issue… Against the repo, there's a couple references to GenAI, still in the repository.
And I assume those should be changed to mainframe, so I opened up.
**Jim Porell** 04:46 Yeah, right.
**Greg Shriver** 04:46 Sure.
But other than that, I'm just trying to get, you know, trying to figure out what's there.
And still kind of reconcile that with, you know, with the open to… with the Federated Semantic Convention model, and what that means for us going forward.
**Jim Porell** 05:03 Well.
**Greg Shriver** 05:04 Thanks.
**Jim Porell** 05:06 I did see somehow we got one of the transaction processing ones passed or least approved. I saw in the notes that Ludmilla, who had been leader of that.
Gave her okay, and then, Antoine went and approved it, so…
**Greg Shriver** 05:24 Approved it.
**Jim Porell** 05:25 At least that's making progress, so that's good.
**Greg Shriver** 05:28 Yes.
you know.
**Jim Porell** 05:30 Well, we'll see.
Well…
**Greg Shriver** 05:33 So…
**Jim Porell** 05:35 Oh, none.
Unrelated, I had volunteered you, in quotes, to join that new open mainframe project.
**Greg Shriver** 05:44 Yeah.
**Jim Porell** 05:45 on the OpenTelemetry. I know they're trying to set up a meeting for next week. They did not include you. They still have Richard, me, and Rudiger on there.
I'll… I'll get you an invite to that, so…
**Greg Shriver** 05:58 I appreciate that. Thank you.
**Jim Porell** 05:59 Sure.
**Greg Shriver** 06:01 No.
Yeah, I don't have anything, anything from you, Robert?
**Pellared** 06:09 Nothing for me, I just was thinking about addressing your issue in the meantime, just trying to address it.
**Greg Shriver** 06:16 Oh, with.
Oh, which issue? Oh, yeah, well, I assigned it to me, but if you want to take it, take it.
**Pellared** 06:22 I mean, I mean, I'll just give it a shot, I'll just try quickly.
Okay.
Not sure how we…
**Greg Shriver** 06:28 Well.
**Pellared** 06:29 I have not noticed that you assigned it to… You assigned it to yourself. I have not… Sorry.
**Greg Shriver** 06:33 But you can, I can unassign it to myself, and you can do it if you want. I mean, honestly, it was something that I noticed as I was perusing the repository, and I figured, you know, this is something easy that even I can figure out. So that's why I assigned myself.
**Pellared** 06:50 So, whatever… do you want or not? However you want. If you want, I can try. If you prefer doing it yourself, yeah.
**Greg Shriver** 06:58 I was just gonna I was just gonna use it as a as a vehicle for me to try and to try.
**Pellared** 07:07 Yeah.
**Greg Shriver** 07:07 Yeah.
**Pellared** 07:08 Okay, so do…
**Greg Shriver** 07:08 Go ahead.
**Pellared** 07:09 Because, yeah, I think it's a good thing just to learn quickly because it should be very straightforward. So, yeah, maybe it's good for you to do it.
**Greg Shriver** 07:18 Okay. Yeah. All right. Well then. Yeah, for sure.
**Pellared** 07:22 Okay.
**Greg Shriver** 07:23 Thanks.
So, yeah, I'm just trying to work through all those issues, you know, on my local machine, and make sure I've got the stuff set up right, and… I still don't understand what… Weaver really is, and… Apparently it needs to run in a Docker container So all of these things are just you know these are things that as mainframe people we really don't do that much So that's kind of, you know… You know, I can learn things, but I probably learn them slower than others.
**Jim Porell** 08:00 I might beat you or be slower.
**Greg Shriver** 08:07 So… All right, cool. Yeah, I don't. I don't have anything else.
**Pellared** 08:13 Yeah, as far as I know, you can also use Weaver locally. I think it's just lots of automation uses Weaver.
in Docker, because it's easier to automate for all operating systems. I'm pretty sure that I saw people using… just downloading the executables, and just use them… using them, so… but… and I… but if I remember correctly, all the things that are done on GitHub Actions.
I'm usually using, you know, Docker for it, because it's just easier to copy and paste. But there is nothing preventing to just, I think, download it as an executable and use it as that, which may be easier for experimenting, learning, because you do not need to mount… Mode volumes, add some permissions, etc.
Yeah, because it's written in rust. If I remember correctly. Yes, and there's nothing preventing using locally. So I'm not sure.
**Greg Shriver** 09:08 Okay.
Yeah, again, I'm, you know, unfamiliar with it, so it's an unfamiliar tool But I… I mean, hearing Antoine speak about it, I mean, it sounds like it's super useful once you understand it, so… Hey, welcome, Danilo. I don't know if I'm pronouncing that correct.
Perfectly.
Well.
Danilo, I think we were just about… Done for this week. We didn't have much of an agenda. We have a couple people that are out.
And, we were gonna close the call down, but we didn't want to do that, you know.
Since you had joined, Just getting started in the community. Okay, great.
Great. Hey, you know, lurking is fine.
Very good. Encouraged, actually.
So…
**Jim Porell** 10:20 And do you have access to… do you have access to the Google Docs? Because that's where most of our meeting minutes are located.
I don't know if you're having trouble getting off mute, or… Oh.
**Greg Shriver** 10:35 I'll shoot the link.
**Jim Porell** 10:37 Okay, you're gonna do.
**Greg Shriver** 10:39 I'll stick it in the chat.
**Jim Porell** 10:44 Oh, wrong room. That's what he's saying.
**Greg Shriver** 10:47 Oh.
Okay, come on! The mainframe is great! You should be here!
Okay.
Well, welcome anyway, Danilo.
**Jim Porell** 11:06 All right.
**Greg Shriver** 11:08 Alright, well, I guess we'll give everybody back 50 minutes then.
And, hopefully we'll see you all next week.
**Jim Porell** 11:17 All right, see you later.
**Greg Shriver** 11:19 Cheers. Hey, good luck, Jim.
**Jim Porell** 11:21 Oh, thanks, Rick. Appreci.
**Greg Shriver** 11:22 Yeah, bye.
**Jim Porell** 11:24 Bye.
**Pellared** 11:24 Bye.
