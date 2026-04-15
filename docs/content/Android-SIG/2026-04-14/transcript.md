SIG: Android SIG
Date: 2026-04-14
Duration: 24 minutes
Zoom Recording URL: https://zoom.us/rec/share/scSPRaBt9pIdmbbnCkIVkNiIL1TIOQfhBBQUFgpfgKJuhAUMQe6opnLrj2DMx_G_.S20Ec1YTUyU7veCh
============================================================

## Zoom Recording Transcript

**Cesar Munoz** 02:06 Hello, David and Cleverchuck.
Let's… Give it a moment to the rest.
**Hanson** 03:17 Lowe.
**Cesar Munoz** 03:20 Hello, Hanson.
**Hanson** 03:21 How's it going?
**Cesar Munoz** 03:24 It's all good.
Good morning.
**Hanson** 03:27 Good early evening.
**Cesar Munoz** 03:32 Thank you.
How's it going with the time zone?
changes.
This year? I mean, hers, they won't change anymore over there, right?
**Hanson** 03:49 It hasn't happened yet, so it's changed now, and the idea is that in British Columbia, they're not changing when the rest of North America goes back to, regular time, in September or something like that, October. So, the chaos hasn't started yet, but it will, in 6 months or so. Less than 6 months, though.
Hey, Jamie.
**Cesar Munoz** 04:16 Hey, Jamie.
Well, at least you get some time, I'm guessing.
probably people are, you know, preparing their software or stuff like that to… it's just like… like it happened in the 2000s.
Or something like that, maybe?
**Hanson** 04:33 Yeah, well, the software… the software is going to be interesting, because we always have, like, Pacific time zone, and that's, like, you know, LA, you know, whatever. Now, Vancouver is different than LA.
So, all the hard-coded, time zone things in the JDK. That's gonna have to change. It's gonna be a .25 for… Or whatever. So, yeah, it's gonna be interesting.
**Cesar Munoz** 05:07 Yeah.
Whoa.
I've heard people complaining in several places that It's no longer needed to have the time zone Daylight savings stuff.
So, I don't know, maybe… trying to be a bit positive here, maybe you guys are just leading the way in the…
**Hanson** 05:32 True.
**Cesar Munoz** 05:33 Or anyone else will follow.
Maybe.
**Hanson** 05:38 That's the idea.
**Cesar Munoz** 05:38 simpler.
**Hanson** 05:41 That's the idea.
the West Coast was supposed to do this, Seattle were, California, Washington, and Oregon, but, they never, they never actually went through with it, so… we'll see.
**Cesar Munoz** 05:58 Whoa.
I'm not sure if… Jason is… What's planning today… to join today, or not? Jason's out.
**Hanson** 06:08 Jason's out, he may be back next week, but I think he, he, I think he's coming back on next Monday, so today he's definitely not here.
**Cesar Munoz** 06:16 Got it. Okay, so I think we can start then.
Let me share my screen. Yeah, I remember he mentioned something about it, but… I just forgot if it was this week or… Anyway.
Where's that button?
Desktop 3, okay.
Alright.
So… This is today's agenda.
I've added a couple of items.
Please add yourself to the… to the list whenever you get some time.
And, well, I just wanted to… Talk about these two issues.
The first one is mostly… it involves JSON, so probably we'll have… we're gonna have to move it to the next, The next meeting.
It's basically the same issue about the stabilization effort for Changing the instrumentation API before making it stable.
it's got already a couple of approvals, and I think… If I remember correctly, Jason was the only one with some concerns about it, but I think… after some changes to the session API from… Jamie, it should be fine.
But, yeah.
I guess it's not too… there's not… there's no point to discuss it without Jensen, because he's the one with the, concerns, so… I'll just move it to the next one.
Later.
Nothing? Not on?
Sometimes English is very complicated to me.
**Hanson** 08:41 Not here works.
**Cesar Munoz** 08:45 Awesome.
**Hanson** 08:45 Thank you.
**Cesar Munoz** 08:48 And apart from that, okay, so, the crash semantic conventions.
I wanted to try and see… I mean, don't get me wrong, Hansen, I think… You have… I… I… I understand the… I think I understand the goal… of… of what's… what's trying to… well, I think… but it's… this is the reason why I brought this up here, because I wanted to… to make sure, based on… on your… on your thoughts on it.
I have a concern about, generally speaking, about, the crash instrumentation, because I guess just to… just to try and… Explain… Better… So… Okay.
I have a concern with our current crash instrumentation.
Because we're essentially using something that's not defined.
And most likely, this name is not gonna… it's not gonna be the… the name that it lands for this event, whenever it lands in the semantic conventions repo.
And my concern is because I believe that alongside HTTP spans, I think the crash instrumentation I see them, too, as the top instrumentations that Like, most projects will want.
to use. And actually, there's an issue… Where some people are already asking about it, for production, And they have concerns.
About, you know, stability and stuff.
And, I mentioned there that really the only concern that I see there is that Most likely, whenever this person has this, and it's mentioned in Kraftos in production, probably whatever query they create, is gonna get affected in the future, whenever the semantic convention lands, because of the name change. I think it's… to be honest, I think it's… I think we can take for… for granted that the name is gonna change. So… So it's kind of like already telling this person that whatever they do right now, it's gonna get broken.
Very soon. So… I just… My concern is that… The longer we wait into defining this name. I mean, to be honest, if there was a way for us to define an event name.
Like, kind of like a… kind of like a… I don't know, like a branding thing that you have to do, just want to have the name.
secured.
And then we figure out everything else.
If we could do that, which I think we can't, that would be awesome.
But, I mean… because of that, essentially what I… really my concern is Not about, you know, whether we should use these attributes or other attributes or not, it's really just the name.
And I… I find that… The changes that you're proposing here.
they… they are doing more than that, you know? They are not only defining a name.
But they are also defining the… Kind of like the structure of two types of crashes.
The ones that we are currently sending, and also the ones that might be needed, or that are… That are definitely needed.
In the future, whenever we are… Capturing, you know, Async type of crashes.
Which… I'm guessing it's mostly for… for the native, kind of, scenarios.
So, I guess… I mean, and I don't wanna, like… I know we're all, you know, we've all probably have a million things to do, And… Funnily enough, I've been trying to use AI to help me lately.
And I just realized that it kind of makes me just try to do more stuff, which in the end is kind of like… it cancels the kind of help that it could provide to you, because now you're trying to take on more stuff.
So, it's… I guess my point is, I'm not plan… I'm not trying to… like… Put any kind of pressure on you, on, you know, trying to kind of merge this, or trying to… Define the perfect schema for… for these kind of events right away, because, you know.
I'm sure you'll… you'll, you'll get there when… when… when you have the time.
But so far, it's taken a bit long, and… what I'm… when I step… when I take a step back.
And try to think about at least what is it that I think we need right now.
Which is just a name.
I'm… I'm just… I'm just starting to think if it's, if it's just worth creating a separate PR that just adds the name and the stuff that we have right now, and then we… this PR will get… will focus more on ex… extending that You know, by adding the async flag in this case, or… Whatever else.
**Hanson** 15:02 There's actually another PR that was gonna come after that was supposed to have the more complicated and controversial ones.
So I think, how about we just move the async to that one, and have this one not include that? Because async anyway was going to be optional, and it was only going to be included, not for the JVM crashes, but for anything that actually was async. So, by design, anything that's not… doesn't have that is… is synchronous. So, the… we could use, what it is, without the async attribute.
For, for what we have in Android right now. And if that's, like, the only point that you have, you know, that you still want to discuss further, I can remove that, put it in the second PR that I was going to submit after this one, and basically wrap that up today, and basically get it in your hands. If there's… besides async, is there any other points that, that, that you want to discuss?
Or that's basically it.
**Cesar Munoz** 16:01 To be honest, yeah, that's basically it.
It's why we still don't have, at least in Otelandry, so it's kind of like…
**Hanson** 16:08 I will… I will remove async today, and get it up to date, and have it, have… have you take a look at it then. How about that?
**Cesar Munoz** 16:18 That would be awesome, thank you. Yeah, at least that way we'll have a name there.
**Hanson** 16:23 The last month has been, Pretty crazy. So I haven't done…
**Cesar Munoz** 16:28 Yeah, I know.
**Hanson** 16:29 much on the open source projects at all. So… but this I need to get done, and it should be able to get done since I already have the whole idea of having two PRs is that the first one's easy, the last one is going to be the one that we discuss a lot. I just didn't anticipate this one to be like that, and actually, it was my fault for not following up, because you already had this a month ago, and I just missed your comment, because I went… I scrolled down to the end, and I didn't see any comments. I was like, oh yeah, you replied to the top, so… That was my fault. I'll get that up to date today, and hopefully we can get it merged soon.
**Cesar Munoz** 17:06 Thank you. Yeah, yeah, just let me know, or, well, I'll see the notifications, I'll just approve it right away, and I think.
**Hanson** 17:12 Yeah.
**Cesar Munoz** 17:13 I don't think I can merge it, but, you know…
**Hanson** 17:15 I gotta do a bunch of rebases, probably, it's been a while. Well, maybe, maybe not. We'll see.
**Cesar Munoz** 17:22 Maybe not. Well, thanks. Yeah, I think… yeah, no. That will… that will just land the name. I think it's really just my main concern, and then after that.
I'll probably create a PR to update the name in the, in OTL Android.
That's good. And then… And then, yeah, probably just add some breaking changes to the change logo.
Yeah.
**Hanson** 17:44 I would say, with respect to what that guy's saying, I think he's asking a much more basic question, which is, is this stable? We have millions of users. And I think the answer is yes.
Because, Splunk and Elastic, and others are… have customers that are productionized on this for a long time.
So this isn't alpha, you know, as in no one's using it.
**Cesar Munoz** 18:10 But code-wise, it should be… should be fine.
Yeah. Yeah, definitely. Yeah, but I mean, after you get the data, you know, then you create some queries around it, so that's, I guess, the… that's the thing that will concern me the most, because then if the queries change, the data changes, your queries get… get broken.
**Hanson** 18:31 Oh yeah, I mean, that's why the instrumentation isn't declared stable, and that's why semantic conventions aren't declared stable. This isn't even using semantic conventions, so once we get that, hopefully they'll, you know… for that particular thing, they will be a bit more, trusting.
**Cesar Munoz** 18:48 I think you're right. Yeah.
Well, thanks, thanks for that. Let me add the notes here.
**Hanson** 18:56 Yeah.
**Cesar Munoz** 19:16 Awesome.
And that was it. From my side. I don't know if somebody else has.
Other topics, or… yeah, anything?
**Hanson** 19:29 Did we do a release?
Because we talked about doing a release last week, I don't know if we actually did a release.
**Cesar Munoz** 19:38 We haven't… actually, this is a blocker for the release.
**Hanson** 19:42 Got it.
**Cesar Munoz** 19:42 And it was added to the, milestone. Okay. Yeah.
So… You say that Jason should be back next week?
**Hanson** 19:54 I think he… I think I made… he made a joke about… well, I… he said he's back on, April 20th. So… so I think he's back by Tuesday, so…
**Cesar Munoz** 20:05 Got it.
Okay, yeah, I think that'll be fine, probably… You know, as soon as this gets merged, or… Yeah.
the… we can create the… the release right away. I don't… I don't think there's anything. I think what the other stuff was… what Jamie already took care of, the, Well, maybe we didn't add it here, but it was related to sessions.
But yeah, so… Actually, yeah, in session.
**Hanson** 20:39 Yep.
**Cesar Munoz** 20:40 Okay, I think we can close this now, then.
Well, we haven't stabilized it yet, probably, yeah.
Yeah. I don't remember, sorry, did you? Okay, you did, set the Boolean?
To stabilize it.
**Jamie Lynch** 20:56 Yeah, I think we just need to set up a Boolean to stabilize it, if everyone's happy with it.
**Cesar Munoz** 21:03 I'm fine with that. I think that your PR is already merged, so… I'll have a look later.
Got it, thank you. So, once… I can probably add that tool in, and we can close that issue.
Cool.
So… Yeah, I think that's it.
So if there's nothing else… Probably able to get some time back.
**Hanson** 21:47 Cool, update the notes with the, what we talked about with the, with the, semantic, and then… oh, you already did, it's just on the next page of mine.
**Cesar Munoz** 21:55 I just moved, yeah.
**Hanson** 21:57 Yeah, no worries.
Cool.
**Cesar Munoz** 22:00 Well, have a great day, and talk to you next week.
**Hanson** 22:05 Yep.
Thank you. Bye.
