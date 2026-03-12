SIG: Go SIG
Date: 2026-01-08
Duration: 45 minutes
Zoom Recording URL: https://zoom.us/rec/share/VWnv6qFiX4KRYimADXX3l4jDI2xo70d4qVkoRVKfvHTs5h44cc9k2QwWCulG6o4S.5SdbGVFpb_Ih_Z5o
============================================================

## Zoom Recording Transcript

**Sonal Gaud** 00:11 Hello?
**Damien Mathieu** 00:18 Hi!
**Sonal Gaud** 00:20 Hey, Damon, how are you?
**Damien Mathieu** 00:22 I'm good, how are you?
**Sonal Gaud** 00:24 I'm doing great.
**Pellared** 00:47 Hello, hello!
Can you hear me?
**Tyler** 00:52 Hey, yeah, I can hear ya.
**Pellared** 00:54 Happy New Year!
**Tyler** 00:55 Yeah, happy.
**Pellared** 00:56 Happy New Year.
**Sonal Gaud** 00:58 No evil.
**Pellared** 01:03 How is the weather for you?
**Damien Mathieu** 01:04 Happy… Happy New Year.
**Tyler** 01:07 Weather's pretty good. Yeah, it's, it's actually just slightly overcast and cloudy today, not pouring on me. So, yeah, pretty good.
**Pellared** 01:16 It started snowing heavily in Poland, like, yesterday, but it makes sense. Yeah?
Yeah, it's even… so, it's, like, 10 degrees lesser in, you know.
Physically, but because it's dry, very dry, and there's no wind, it's even hot… kind of, you know, you feel it's hotter than usual.
**Tyler** 01:41 Right, yeah, yeah, the humidity makes a big difference, for that, especially the cold, right? Yeah.
**Pellared** 01:47 Yep.
Okay, attendees, please.
**Tyler** 01:58 Damien, how's the weather in France?
**Damien Mathieu** 02:00 It was cold, the beginning of the week, but it's better now.
**BhupinderSingh** 02:05 Rainy, but yeah.
**Damien Mathieu** 02:06 And by court… by court, I mean… no, I mean, it's… there's been snow, but not here.
**Pellared** 02:13 Because then I'm on the south, right? Or am I…
**Damien Mathieu** 02:16 Yes, yes, I'm in the south. The snow is… was like… Paris was under the snow.
Yeah.
it's like everybody's lost, but the temperature is actually what was, like, a normal winter when I was a child. So, yeah.
**Pellared** 02:33 Yeah, same here.
**Tyler** 02:39 Brian, I'm guessing you've got just a bunch of rain like, like me?
**Bryan Boreham** 02:42 I do, Yeah, I mean, same as in France, I think it was cold at the beginning of the week.
And a little bit of snow.
But it's just raining right now.
**Tyler** 02:56 Yeah.
Yeah, that and for the next 6 months, yeah.
Well, cool. Yeah, we can jump in here in just a second. If you haven't yet, please go ahead and add your name to the attendees list. If you have agenda items you want to talk about, go ahead and add them as well, and I'll start… Sharon here.
Let's see if this works.
**Sonal Gaud** 03:23 If you guys don't mind, can I start with my introduction?
**Tyler** 03:28 Yeah, sure, go ahead.
**Sonal Gaud** 03:31 Yeah, so, hey everyone, I'm Sonal, I'm from Mumbai, India.
And I'm right now a full-time software engineer at Essential.
And I've been contributing to OpenTelemetry, I guess, so it's been a year now. And I've been a member for, like, 8 months. I have been contributing to Go, Contrib, Go, and Collector, mostly.
So, yeah, that's it from my side. Happy to see you all.
**Damien Mathieu** 03:57 What's coming.
**Tyler** 03:57 Yeah, welcome.
Happy to have you here.
**BhupinderSingh** 04:02 Hi, guys. Bupinda, this site, from India, Chandigarh.
And I've been working with New Relic, and recently started working with OpenTelemetry for a client.
And recently, I joined, to support, you know, up and elementary, so I can contribute.
to few of the projects, my, like, I have taken up one task in .NET.
And I'm going through the meetings to understand more into it.
Happy to be here. Thank you.
**Tyler** 04:35 Yeah, welcome as well.
Good to have you both.
Okay.
Cool, let's see if this works today.
Nope. Alright.
Okay, cool, sorry. Yeah, Zoom is, depending on the upgrade, working or not.
Awesome. Alright, so, yeah, I just wanted to jump in here. I think the first thing I have on here is somebody else added it, but, I'd hoped that we could do something like this and just go through a little bit of a planning, session here at the beginning of the year.
And maybe talk about.
what we want to accomplish. I know it'd be nice, since we have especially some newer folks on that maybe are talking with, end users, I'd love to get some feedback on that.
But to start, maybe we can just look at what we did in the beginning of last year in talking about trying to accomplish things.
So, I think that we can maybe just go through this. The new SEMCOM stuff with Weaver, that was accomplished pretty early on. The rest of the stuff, so we had the SDK self-observability signals, the Go runtime metric stabilization, the logs API stabilization, OTel HTTP stabilization, and then file-based configuration.
So yeah, I think that there's… I think a lot of work was made on all of these things. I don't think any of the ones that aren't checked are done, unless I'm misunderstanding that.
**David Ashpole (dashpole)** 06:18 No, I don't think so.
**Pellared** 06:19 You're correct.
**Tyler** 06:23 I do think that we're… we're pretty close on a lot of these, so I think that the question was if, we want to… continue on with these goals, and I think that that's fair.
But maybe what we can do is, try to recreate this, I don't know if this is gonna work.
Yeah, kinda didn't. I don't know why this one's not picking up.
So maybe, we could just start here by saying, like, are there any other, I think.
things that we'd like to accomplish in this year, and if so, then, we can… we can look at, you know.
What?
Oh, man.
Alright, that's all checked up, but whatever. Okay, so… I think these are really great goals, I'd love to keep working on these in the new year. Any other ideas or things that people would like to see?
**David Ashpole (dashpole)** 07:53 I don't know if this belongs in goals. I opened an issue about the performance of the attributes package. I don't know if it's ready to be… Set as a goal or something, but.
**Tyler** 08:07 Yeah, I think we maybe just consider this more of a brainstorming session, so I think that that's, fair. So, I'm guessing this one right here?
**David Ashpole (dashpole)** 08:14 Yeah, yeah. Maybe it's a good time for me to just share the work I did over the break.
**Tyler** 08:19 Okay. But…
**David Ashpole (dashpole)** 08:20 the TLDRs that… We've made the actual SDK a ton faster.
But creating your attribute set, to pass to the SDK.
It's like… 10x the performance cost and an allocation, no matter what you do, of the actual increment.
So… it, Yeah, when I realized this, I put a little bit of a wet blanket on it, on some of the work, but that being said, this is something that I'm definitely interested in, and… I'm still looking for ideas for, so I don't know if that's, like… The right thing to put on our roadmap, but… Yeah, I think… I'm not sure what the solution is yet, but I think, improving the attributes package, if we're gonna do any work that's, like, performance-focused, I think that's, like.
probably the best place for us to invest our time. I assume this also has similar impacts for, like, logging or tracing as well.
**Tyler** 09:27 No, we don't use sets there.
**David Ashpole (dashpole)** 09:31 I see…
**Tyler** 09:33 Yeah. Robert, this is something that's… it's very unique to the metrics package.
**Bryan Boreham** 09:39 So… I think there's some kind of knock-on effect, because I've noticed this in profiles, I think when you're intending to use, like, the tracing integration with gRPC or something like that, it creates some metrics internally.
Which then pay this cost.
**David Ashpole (dashpole)** 10:00 That's because we don't have the enabled API yet, so there's going to be an API where, basically, before you make your attributes, you can check to see if the instrument's actually turned on.
And avoid that cost in the future.
Yeah, you're right, that it does… at least, it actually…
**Pellared** 10:18 In logs, we are also using the attribute set in the scope.
But only the instrumentation scope.
**David Ashpole (dashpole)** 10:26 Only in the scope.
So, our other APIs, do they accept just… After Stone's beats.
So is the… is the change just to get rid of attribute set?
Deprecate it and add a… They can't…
**Tyler** 10:45 You can't do that because metrics are defined on an attribute set. So a data stream is defined on a particular collection of attributes.
So you need some way to represent that.
And you need some immutable way to represent that.
**David Ashpole (dashpole)** 11:04 Okay, I'll need to take a deeper look then.
Yeah, so this is on my mind after the break, but I don't think we need to include it in goals until we actually have a plan.
**Tyler** 11:15 Okay.
For what it's worth, I have looked at things that you're looking at, this constructor idea as well.
The immutability thing becomes a little bit harder.
Yeah.
Yeah, the immutability thing becomes hard because, at the end of the day, you still need to do some sort of new memory allocation to have the new set so that you don't mutate the old set. Whether that's extending the memory and doing some, like, things internal, maybe? That's maybe a possibility.
But you still need to have the old… like, set remain comparable and remain immutable. And so, like, there's, like, some underlying, like.
deep underlying issues as to, like, what we need from this that are hard to get around for the performance issues.
I think that… a lot of the performance issues go away if you write instrumentation correctly, like.
to not use… That's what I was…
**David Ashpole (dashpole)** 12:21 So that's what I was trying. It's like, the only way I could get it to be performant is if I created my attribute sets all ahead of time, and just referenced them, right? Yeah.
But for…
**Tyler** 12:33 not great if you have something dynamic, right? But yeah.
**David Ashpole (dashpole)** 12:35 So, basically, Which, it… Unfortunately, seems like even most of our self-observability telemetry all is, right?
And that has, like, weird knock-on effects, where I'm pretty sure…
**Tyler** 12:50 Well, only in error cases, it's…
**David Ashpole (dashpole)** 12:52 I mean, Eric. Okay.
**Tyler** 12:53 Yeah.
Yeah.
Because, like, all of the happy path locations, like, those are static attributes, for a particular thing that we can know a priori, like… And that comes from the fact that, like, you really want to be able to know them, because otherwise you have, like, carnality explosions if you're doing these dynamic things. So, in theory, that should work, but yeah.
There's definitely… I've thought about this a lot as well. Like, I like the idea of a constructor. I'm also, like… I mean, I'm also… I'm not opposed if we wanted to completely, like, have, like, a different… Type, like, like, really thinking outside the box, like.
Instead of having, like, right now, the metrics Except attributes, attribute sets, and then if we want to, like, add a third thing?
And that third thing is somewhat optimal. I think that'd be great. The problem is that, like.
Yeah, I just, like, I can't figure out how to do the third thing, and, like, even if you try to do some sort of lazy evaluation, like, you still, like, you have to compute some sort of hash or something, because you need to immediately, you need to use that to distinguish it from other sets, or to classify it, essentially. And so, like… there's always going to be, like, intrinsically something there that needs to, like, look at the comparison of a set, and so that's always, like, I think the thing that comes back to… It being a hard problem.
**David Ashpole (dashpole)** 14:20 Yep, I think that's fine. I… somehow Prometheus does this, so it's like, I know it's possible, and we should be able to maybe look at how they do it, but…
**Tyler** 14:31 I don't think they're as stringent on, the mutability side?
**David Ashpole (dashpole)** 14:38 No, because you just pass in…
**Tyler** 14:40 Right.
Well, yeah, or a slice of strings, right? And so it's like, I think… Yeah, and I think that that's, like, where we made the difference in, like, in trying to distinguish, like, these immutable sets being immutable, and trying to make sure that they actually were immutable.
And comparable, I guess.
I mean, I think that's the other thing, is, like, actually, I don't know what the API for Prometheus is anymore, but, like, it used to be just string-string labels, right? And so… You also have to contend with the fact that, like, you have different types of labels, and that, like… Yep.
Yeah, there's, like… and then taking that and then turning it into a comparable key is, hard to do without… Some proprietary data format to, like, you know, put that into memory the way we do it, right?
So, yeah, I mean, I think, like, I think this is a good… like, I say this is, like, my least favorite package out of everything we've ever released, is the attribute package.
And so I think this is one of the main reasons why. But yeah, happy to continue looking at this with you.
**David Ashpole (dashpole)** 15:49 Okay, cool.
**Tyler** 15:51 Yeah.
Cool. I remember also at the beginning, or the end of last year, Brian, I had asked you, like.
As more of, like, an end user, like, did you have things that you want to see come out of this project over the next year?
even, like, things that maybe are beyond our control, but, like, yeah, just… I think you had mentioned a few things, something like that, last year.
**Bryan Boreham** 16:19 Okay, my mind's drawing a blank right now.
**Tyler** 16:23 Yeah, I think it was something, like, you wanted something in the collector, and that collector had a dependency on us, and I can't remember exactly what it is, sorry.
**Bryan Boreham** 16:33 I mean, that…
**Tyler** 16:34 Like, a blank.
**Bryan Boreham** 16:35 I… That sounds like, like.
**Tyler** 16:40 Well, I mean, I guess you already gave us one, the enabled method and metrics, right?
**Bryan Boreham** 16:46 Yeah?
Yeah, I mean, there's layers to all these things, I, I… so, Yeah, I spend a lot of time worrying about performance, and maybe that's not what most people really want. But, so I think when you… when you… something that I said about the collector and the library and so on, I think, was about the, protobuf serialization.
which, the code for that is in the collector.
But it gets used wherever you're… wherever you're, sending.
telemetry.
**Tyler** 17:34 The protobuf serialization.
Yeah, I'm not… I'm not sure I follow. Like, I think that that makes a lot of sense to have an optimal protobuf serialization But I don't know how we're involved in that one. I can't remember how that was coupled.
**Bryan Boreham** 17:54 Well, yeah, I mean, in practical terms, you're not, because it's in the collector repo, but…
**Tyler** 18:00 Yeah.
**Bryan Boreham** 18:00 logically, that's not the way I think about it. You know, I… I think… Yeah, I… the… so the split between the various, hotel sub-projects that own bits of this is not clear in my mind, so that's a me problem. You know, not really a you problem, but…
**Tyler** 18:22 Yeah.
**Bryan Boreham** 18:23 As an ignorant end user, that is one of the things that… happens a lot, is I… I think, oh, I should ask a question about this, and I ask it in the wrong place. You know, I don't think that's a… that's not something you'd chalk up as a goal for the project, or something like that, but it certainly happens.
**Tyler** 18:45 Yeah, indeed, it does. And I'm happy to have it happen, and happy to direct and facilitate if needed, and get you in touch with the right people as well. Like, I don't think that you should feel… any sort of hesitation in trying to ask these kinds of questions. So, yeah, okay, that makes sense. Maybe that was what we were talking about, yeah.
But, okay.
I'm gonna remove this, because we talked about this one, wait on that one. Okay, cool.
I can, I think this is a good seed set for this. I'd also maybe say that why don't we try to, wait maybe a week and talk about this and think about this asynchronously?
And come up with other goals, maybe look at other things. I know that there's also things at the specification level that we probably want to take a look at what's active there, and maybe, you know, populate this goal list. And… and then maybe what we can do is… I think try to finalize, our, our goal list for this upcoming year in the next week, at next, meeting. So essentially, like, act as this upcoming week, think about a brainstorm, and then… Next week we can try to filter this down.
what do people think about the best place to locate these goals? Is this document the best place for people to just keep adding to, or is there another place?
I can't see anybody, so I don't know if they're making any gestures, but if, if that's not the case, why don't we just do that? If you… if you want, please just keep adding to this section that I've already added here, goals that you want to see, or you think are important.
That we should try to achieve in the upcoming year. And then, yeah, next week we'll start off the meeting by going through these and then trying to prioritize based on, Expected developer capacity.
Okay, next up, Damien, you wanted to talk about, Linux Foundation membership projects?
**Damien Mathieu** 20:52 Yes, actually, I was pinged by Sonal, yesterday.
And she was asking whether we had, projects for LFX mentorship.
And, thinking about it, I thought maybe hotel HTTP stabilization could be a nice project. It has a lot of side things to do, not all of which are fully defined, so it's not, like, just, Ticking checkboxes, and yeah, I wanted to gouge opinions about submitting an LFX project for this one.
**Tyler** 21:36 So what sort of, developers are going to be included in this project?
**Damien Mathieu** 21:43 It's students. Students.
**Tyler** 21:45 Okay.
**Pellared** 21:47 That's… Then, Damien, you will be a mentor?
**Damien Mathieu** 21:50 Yes.
**Pellared** 21:51 Okay.
**Tyler** 21:53 Yeah, so my hesitation is the… what you just described is a lot of these things aren't, like, checkbox things. They are… like, think through topics, think through API design, think through, like, packaging structure, and think through use cases to, you know, produce the best API that we can in this package.
And I'm, I'm hesitant because in the history of us having, like, interns come in or students come in and work on these types of problems, like, we don't… it's not… It takes longer to… Explain and go through and think through a lot of the solution space than it does to actually… Just do it yourself, I think.
And so that's… I think that's my hesitation here, is if… You think that that makes a lot of sense for your time, and that, like, you're willing to, like.
walk through these things and take, you know, more time than it would have taken you to do this in, like, your own. I think that that makes sense. The problem is, is that, like, we've seen this… Before… I think there were, like, 2 other times we've tried to do this, and, like, it turned out to be a lot more of a headache than it was to actually just go and do them yourself.
So, I… that's my hesitation on this one. If we can… if we can define these as checkbox items, I think that that's, like.
a great candidate, then. I think that if you can give specific tasks on, like, what to do for new developers, let alone, like.
this LFX mentorship thing, but, like, also just… just new folks, like, I think that's a great way to do it, but yeah, I… I mean, I…
**Damien Mathieu** 23:32 I think if we can define that as just checkboxes, we don't need an intern. We just need to have issues that we tag as good first issue, and we will have people picking those up.
I think the… yes, having an intern takes more time, but that's, like, I guess, different thinking and a learning experience for them, it's, yeah, I mean, as a former student, like we've all been, I suppose, if you give me an internship where I only have to tick check boxes, there is not much value added to that.
**Pellared** 24:13 I'm with Damien here. I also do not, like, maybe just to make it… clear. I do not think the goal of the mentee should be just to complete everything. I think the goal of mentorship is just to help into, you know, basically, you know, helping and make, basically, like, improving our, you know, kind of software engineering, you know, world connections, etc, and just making sure that developers know how to even think, how to design, and I think some of these are very hard.
and probably it will be on you, Damien, just, you know, pick up the ones that are easier, and just, you know, kind of, you know, mentor and help a lot.
Here.
I think it will be more than mentoring, basically. It will be more like even… Teaching.
I would say.
**Damien Mathieu** 25:09 I mean, I see that as, like, having frequent discussions with that person, and just, like, Figuring things out together.
**Tyler** 25:22 Yeah, it's also gonna involve a lot of community interaction, and, like.
You know, that… that is something that, like.
I think having existing relationships is going to be important on… So, I think maybe the question is more, like, did you want to scope this down to particular issues? Because I don't think that it's realizable to, like.
**Damien Mathieu** 25:46 Yeah, I mean, I definitely do not mean this, and all of it is achievable by a mentor, a mentee. Yes, I agree. I think it's, like, yes, we need to scope it down.
Yes.
**Tyler** 26:03 Okay, and then is it just one, candidate that's going to be working with you, or are there going to be multiple?
**Damien Mathieu** 26:08 No, I… yeah, one is going to be enough, in my opinion.
**Pellared** 26:13 As far as I know, it's usually 1.
**Tyler** 26:17 We should clarify that. That hasn't been the case in the past.
Okay. So, yeah.
But I, I mean, Damien, yeah, if you're… I think this is assigned to you. Well, it should be a… okay, you opened it.
Yeah, I mean, if you.
**Damien Mathieu** 26:33 I mean, we can assign it to me if we wish, but yes.
**Tyler** 26:37 I mean, like, however you want to, like, go about this, that makes sense to me. I'm just… Yeah.
I do know that, like, we've had issues where we had a lot of, reverts from things… from people that have done this in the past, and it was because I think there was a lack of mentorship in that intern process, and so I think if you're willing to take on that responsibility of a mentor, I'm happy to be confident in your, yeah, you going forward.
**Pellared** 27:06 Because, Tyler, I think previously, no one from our GoSeq was really a mentor.
**Tyler** 27:12 Exactly, that's what I'm saying, yes.
**Pellared** 27:13 Yeah, so it's a different thing, yeah.
**Damien Mathieu** 27:16 My thinking is also to write down in the application that we need someone who can join the SIG meeting.
**Tyler** 27:25 Absolutely, I agree. Yeah, I think that's gonna be critical to the success of this, yeah.
Well, cool, yeah, I mean, I think that that makes sense. I think that… that also motivates us to continue, the OTEL HTTP stabilization effort as our plan for this next year, so keep that… keep that work going. So, that sounds great.
**Damien Mathieu** 27:48 Yeah, so, yeah, I'll draft a, thing, and if you want, I'll share it with, in the private Slack channel before submitting, anyway.
**Tyler** 27:59 Okay, sounds good. Thanks, Damien.
Okay, Robert, you want to talk about logs to reuse, attribute key value and remove the log?
Key value types.
**Pellared** 28:12 I was just, you know, this tab… this… the stabilization specification here was merged yesterday.
So, I think we are safe to work on it.
So, my plan is just to start working first on the attributes package, add the new types, the empty type, the, I don't know, buy slices, the maps, arrays, probably one PR per type.
Just to make it, you know, baby steps. And I just wanted to ask, first of all, do we plan to make a January release? Just to make sure that we do not merge any of… maybe you can merge maybe empty, or some attributes, but yeah, just to make sure that… We just do not have some, you know, strange state when we have, you know, something only in the middle.
**Tyler** 29:00 Yeah, I think… first off, I think it's great to see this. I'd love to see that work, move forward, like you're talking about. I think you're also thinking about it very pragmatically, so I think that that's a great question, is if we want to get a January release out.
This is interesting.
**Pellared** 29:22 You just give it yourself.
Thank you, huh.
**Tyler** 29:30 Yeah, I don't see anything blocking…
**Pellared** 29:32 I think so.
Has Carlos added this support?
**Tyler** 29:36 Yeah, yeah, yeah, we just need to prioritize doing this. Yeah, I'm just saying there's not a broken state here. It just looks like an easy task for… a relatively easy task that we can try to get done.
It looks like the sync map for Atomic for fixed bucket histograms got merged. That'd be pretty nice to get out. David, is there any other…
**Pellared** 29:58 reservoir.
**Tyler** 29:59 Yeah, yup, histogram Reservoir.
The last value…
**Pellared** 30:05 Oh my god.
**David Ashpole (dashpole)** 30:06 I mean, yep, there's some stuff in here.
**Pellared** 30:09 That's great.
**David Ashpole (dashpole)** 30:11 There's plenty more open, too. So, there'll be… Yeah, steady.
**Tyler** 30:15 Is… open that we would try to get in?
This is fun.
**David Ashpole (dashpole)** 30:20 Pretty close.
I think the ones that are probably the best candidates are all the reservoir-related ones. I don't know if… I don't remember… The exponential histogram one is just gonna take some time, and I'll probably try and split that up as much as I can.
**Pellared** 30:35 Yeah, that one's next.
**David Ashpole (dashpole)** 30:38 And then, if people remember, there's the change to histogram reservoir to make it, time-weighted, or time-based. That… that I closed, but I'll reopen once the optimized fixed-size reservoir is in.
**Tyler** 30:54 Okay. Do you remember that at all?
**David Ashpole (dashpole)** 30:57 It was a spec PR, not a PR here.
**Tyler** 31:00 Oh.
**David Ashpole (dashpole)** 31:01 Basically, like, currently the fixed bucket one is time-based?
is time-weighted. And then the histogram one is always keep the latest for each bucket.
But it's changed.
**Tyler** 31:13 Oh, right.
**David Ashpole (dashpole)** 31:14 Time weighted for each bucket, yeah. And it's actually a performance improvement, because… It is?
If you have a… because the expensive part is actually overwriting The…
**Tyler** 31:25 Oh, okay, so you're not gonna overwrite every time, it's more…
**David Ashpole (dashpole)** 31:27 Since you're not overwriting every time, it's way cheaper when you have large numbers of observations, yeah, so that's…
**Tyler** 31:32 Yeah, interesting.
Yep. Yeah, first, first look, I would have guessed opposite, but okay, that makes sense, yeah.
**David Ashpole (dashpole)** 31:37 That's what I guess, too, yeah.
Until I did.
**Tyler** 31:40 Cool, alright. Yeah, so, so Robert, to answer your question about the release, I think that, we could try to get this optimized fixed-size reservoir in.
Looks like it's waiting on… My review… Three weeks ago. Okay, so I just haven't taken another look at this. So yeah, I… I don't know if we want to try to get this in. I… are… is there anyone… Who's looking to do a release today or tomorrow?
Or has the time to do the release, out of all the maintainers on the call?
I can probably get one in next week, if that's the case then. So, why don't we try to do that? So, Robert, maybe… Yeah, let's just try to get a January release out, let's try to get these fixes. Let's maybe also try to get this prioritized to get reviewed, so I'll add it to the milestone.
And, yeah, let's get a release.
**Pellared** 32:41 Since there's no… there is no rush for adding these attributes. I was just asking, you know, January… Yeah, I also can also… R.
Next week is also good.
**Tyler** 32:54 I think, there's a rush in my mind, because I'd love to get that logs API stabilized, and that's a… that's a big blocker.
So, yeah.
Okay.
Cool, then let's… let's do that. Let's have that plan. I'm… I'm excited to see this.
**Pellared** 33:12 I'll also have assigned to myself, making the enabled functions of the synchronous metrics, asset metrics, to make them stable, because I know that Collector uses it, so it'll be a very small PR. I would also try to include it in this release.
**Tyler** 33:32 In the specification you're talking about, stabilizing it?
**Pellared** 33:35 it's stable already in specification, so we can export it in our metrics API.
**Tyler** 33:43 Oh, cool.
Yeah, sounds great.
**Pellared** 33:45 Okay.
**Tyler** 33:48 If you open an issue for that, could you maybe link to this so that we can…
**Pellared** 33:53 I will give you… I'll do it in a sec.
**Tyler** 33:56 Yeah, cool, sounds great.
Okay.
That's the end of the agenda, so I'll pause here. Any other topics people want to talk about?
**BhupinderSingh** 34:08 Huh.
One thing, from my side. So, I think, if it would be great if I can get some topic, where, I would feel more valuable next time joining the meeting, which would be a help for you guys, I can… I could research upon.
While we wait for next meeting.
Or in the chat, I can… if you guys can provide me in the chat Slack channel, that would also be great.
**Tyler** 34:37 Are you looking for an issue to start working on, is that what you're saying?
**BhupinderSingh** 34:42 Yeah, any, like, issue or any research topic you guys want me to do?
Like, any sort of task.
**Tyler** 34:50 Yeah, so, I mean, I think… we'll have a little bit better of an understanding of, like, the prioritization next week, given our goals are still being set for the year, so I think that… If you're asking for things that are gonna have, like, moving the needle towards our goals, like, we're still working on defining those.
if you're looking for particular tasks, there's definitely… there's tons of issues to just jump in and take a look through and see if something sticks out to you. Yeah, if there's something there, like, you're obviously welcome to start working on it. I would say leave a comment that you're gonna start working on it, or double-check that nobody else is working on it, and then we can assign it to you, is usually the process there, if you find something. I think another thing, specifically for, like, new developers that's really helpful for us, is if you can, Yeah, find gaps, I think, in our existing, documentation, or understanding of the repository, so things that, like, aren't obvious to you are pretty helpful, because there's a lot of, I think, things that won't be obvious to people, so if you can find those and document them, or just work on those in PRs, like.
Organically, that's always great as well. So, that's where I'd say to start. We could probably talk more about specific issues around, like, our goals.
as you saw, like, Damien is looking to stabilize the OTEL HTTP semantic… or, instrumentation package, which has, like.
Tons of issues in it, but, like.
we would like to work on those as well. So, yeah, I think there's more to come there. Also, yeah, take a look at the contrib repository.
**Pellared** 36:20 Totally.
Personal opinion, this is how I started, make code reviews. It makes them even your… it helps others, and also makes your contributions in the future easier, because you'll see what other commenters are commenting on, and also what are the patterns that we use, etc.
**BhupinderSingh** 36:43 Sure, yeah, we'll do that. Thank you, guys.
**Tyler** 36:51 Cool. Any fun projects people worked on over the break, by chance?
I did a lot of knot coding, so… I don't have anything to share.
**David Ashpole (dashpole)** 37:04 I started writing a blog post, and then… Stopped writing it after, discovering that new set was 10x the cost of the metric API call.
**Tyler** 37:17 Yeah.
Yeah, I mean, now maybe you see also why that, like, with attribute, option is completely useless, given it makes a new set every single time, even if the set already exists. Yeah.
Yeah.
That was actually something that, like, I had a proof of concept on, like, since we were doing, like, a hashing structure, I also had, like, this proof of concept, David, where, like, we had, like, a centralized, like, memory store for all, like, attribute sets that have ever existed.
And anytime somebody asks for a new set, it would first ask, like, hey, does this, like… You would hash it, and you'd say, like, does this set already exist? And if it does, you would just return that set.
as you can probably guess, like, there's some problems there, around, like, synchronization and, yeah, just some bad things that can happen, so… Yeah, I don't know, like, I really don't know the right answer there, but yeah.
**David Ashpole (dashpole)** 38:11 Okay.
**Tyler** 38:15 But yeah, you could also just juke the stats on that blog post and just, you know, write things with really simple attributes that are always reused from the start, so, yeah.
**David Ashpole (dashpole)** 38:24 I was hoping not to do that, actually.
**Tyler** 38:27 I know.
I know.
Yeah, it's kind of annoying, but it also, like, I think that's also why, like.
The… the amount of work that we put into, like, the self-observability stuff was, like, so important, because, like.
Without it, like, the SDK would have just become… very… very high performance overhead simply by turning on, like, observability metrics, so, yeah, I think that's… Yeah, important to think through. But it also is, I think, maybe more, like, a great example of, like, why… until we can figure out a way to, like, get around that, maybe we need more documentation and more blog posts on, like, why you need to be writing instrumentation in a particular way, and trying to, like… You know, I think we did that in our… in our…
**David Ashpole (dashpole)** 39:14 contributing, or… Yeah.
**Tyler** 39:16 Yeah, our docs, where it was, like.
here's, like, 5 strategies to try to, like, avoid, creating dynamic attributes. You should try these before doing that, yeah.
**David Ashpole (dashpole)** 39:26 Yeah, yeah. But the fact that it's… if we did write this documentation, it would be, like, the same length as all of the rest of our documentation combined.
I think, to me, just, like.
Points out how, like, how hard it is, at least for users today to write.
optimal… you know, metric code with our… with our API and SDK.
**Tyler** 39:48 One thing I also, I looked… What's up?
**David Ashpole (dashpole)** 39:55 I think Robert froze, maybe?
**Tyler** 39:57 Yeah, I think I put him in purgatory somehow.
Yeah, I don't know what happened. But one of the other things maybe I can mention is, like, I did look at, like, using, like, a custom C API to try to handle this, and it was, So, it's a horrible idea, one, because then you need, like, Sego, and then, obviously you have to manage your own memory, so it was, it was, abandoned pretty quick, but just, yeah, interesting to think through, yeah.
**Pellared** 40:25 Okay, I will… my connection was lost, but I'm back. Okay, there he is.
Not sure what was the reason why I should not talk anymore. Okay, I just have a question. David, do you think… is there… is there a good place, or maybe any one of you, for making some, you know, kind of instrumentation guidelines, or things like that, you know?
How to write instrumentation.
Should be in package comments, or documentation, or…
**David Ashpole (dashpole)** 40:55 I think we definitely should write it. Like, I've been hoping that our… now that… when Tyler initially, or whoever wrote the initial docs for how to do our self-observability metrics. My comment was, like, this belongs on OpenTelemetry I.O.
But I think now that we've kind of proved it out a bit, and applied it to a bunch of different places, maybe that makes a lot of sense.
I would love if it was easier to follow.
But… Yeah, I think that…
**Pellared** 41:29 I think OpenTelemetry I.O, or package… just, you know, package documentation? Or just, you know, for instance, pack… open telemetry I.O, but you will reference just it from the package documentation.
**Tyler** 41:43 I think OpenTelemish.io is the right place. I think that's the place that the project tries to centralize docs, I think that's the place that you can reference from.
**Pellared** 41:50 You can render it better, it can have better visuals, you can have stuff.
**David Ashpole (dashpole)** 41:54 I think that the problem for package documentation is mostly that this is, like.
a cross-package problem. Yep. It's like… it's a combination of the metrics API and the… Or, like, actually, if you were to put it somewhere, it would be in the attributes package, but almost nobody who's writing metrics is going to be looking at that particular package.
**Pellared** 42:16 Okay.
**Tyler** 42:23 Okay. Well, cool. Thanks, everyone, for joining. We can probably end the meeting early here. We will see you all in a week's time. Please think of goals and things you'd like to see done, and if you have them, please add them to that doc, and then we'll talk about it next week.
Until then, talk to y'all later. Bye.
**BhupinderSingh** 42:39 Thank you, guys.
**Sonal Gaud** 42:42 Thank you, boys, bye.
