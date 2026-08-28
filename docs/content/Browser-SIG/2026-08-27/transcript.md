SIG: Browser SIG
Date: 2026-08-27
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Jared Freeze** 01:46 What's up, everybody?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 01:49 Hey there.
**Jared Freeze** 01:55 Open Drive today.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 02:00 If you don't mind, that'd be great, yeah.
**Jared Freeze** 02:04 Yes.
It's just David.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 02:10 Damn.
Just quickly, I'll be, I'll be, out next 2 weeks.
So I won't be able to attend next week's.
**Jared Freeze** 02:22 Okay.
Girl.
Cool, alright, it's 1133.
We can do sort of informal at the end, since the only official thing on here is savings. But yeah, you want to go ahead?
**David Luna Bistuer** 03:10 Yeah, basically, just to bring to your attention this issue that I created. Basically, I remember that we were discussing about, Unifying, configurations, or at least from the, apply, resource. Apply custom attributes for block records.
That many, different instrumentations have the same, so I, I just noticed that both instrumentations for network They have almost the same configuration.
So, I was thinking that maybe, I don't know, just wondering if it was worth it to have, some kind of, Similar, or at least the… you know, not identical, because they're not doing… they're different APIs, but… As close as we can for configurations, and then maybe in the future, we want to have kind of a single configuration for for the SDK that spreads on the different instrumentations, and we can prioritize this. So, basically, what I found out is, like.
Most of the properties are the same.
Specifically, the ones that it includes for propagation and in our URLs. I think that the only one that's missing is a request hook, that we could do something similar.
Okay, so, yeah, that's kind of a question.
And the earth to sea.
If you see the value in that.
If it's worth sticking it, or maybe we can just close it and take it for later assist.
What are your thoughts?
**Jared Freeze** 04:43 I'm gonna go a step farther and say, why do we have two instrumentations?
if they're gonna share a config, and they all do networking, and they all generate the same things, what is… what's the point, right? Like, I get it, no, it doesn't have XHR, but we do, right? So… Is that worth talking about? I mean, does anyone… I mean, truthfully, like, do you care? Like, do you care if it's XHR or Fetch if you're doing networking?
Probably not, you know, as a consumer, using the SDKs.
I don't know, that's kind of where my head went, if we're gonna try to… have a man… like, why have a manager if you don't need one, right? So… I think that's kind of my first take here.
Oh, that was a huge change, but… yeah.
**Joaquín Díaz** 05:33 Yeah, I think for now.
I think for now, we should keep the same API as close as possible to what we had.
I think it's a valid question.
But also, Like, each of the… that Joaquin… APIs have, like, their own… things that we have to fix on, like, each of the instrumentations do their own things, so I don't know if we want to have, like, a big instrumentation doing too much things.
I agree we should share as much code as possible.
Yeah, I don't know. Also, like, you might not care about XHAR, like, if you know your application is only fetch, and maybe you don't want to have, like.
third-party libraries using XHR showing up is one way of doing it.
Balio.
I wouldn't say in the future it's not an option.
**Jared Freeze** 06:35 Yeah, I mean, I was just thinking, like, you know, if you're gonna share config, you could just do something like XHR false. Now, you would be shipping some init function that, of course, does the patching.
you know, that doesn't seem too big. That may be a convenience people do not want, but… But yeah, I think this makes a lot of sense, you know, just in general. Like, it should share all the same things. But again, that's why I'm bringing this up, is you're gonna share all the same config, you probably want all the same outputs, so… I don't know, you got, you know, you've been on this project a long time, David. What do you think?
**David Luna Bistuer** 07:16 Hmm. Well, I like the way that the things are read right now, not because I'm comfortable with, but It's just augmentation is just taking one API and actually doing instrumentation around it.
So it's specific to that. Maybe we can just, Or something that we can do is, I think it was… Kind of a similar situation with, with, with, contrary instrumentation that was… we had.
I think what's Redis? Redis and Redis 4.
And then what we did is, like, okay, we merged that… those instrumentations, although the implementation is separate, there is something, you know.
There is, an actor on both on top that actually… Decides which instrumentation is acting on that, and then accepts just a single configuration object, so we can do something like that.
But still, I would keep the code separate. Instead of just make it as just a networking simulation for everything related to the network, maybe we just keep, like, the small classes.
We have the small classes, we have the thorough tests, then maybe we can do something that actually orchestrates between them.
I don't know if this is something that should live in the instrumentation or the SDK?
But yeah, it could be a good way to move forward.
**Jared Freeze** 08:33 Yeah, I mean, it makes sense to be in the SDK, you know, and then have the config mirrored, because some people are going to use instrumentation without the SDK, that's fine too. I mean, I guess we have a commitment to deliver whatever's smallest, so maybe combining's not… you know, is against the rules, or whatever.
Yeah, Trent, do you have input?
**Trent Mick** 08:55 Just… a parallel thing not to consider, because I don't think the browser's going to be jumping on declarative Config stuff at all, but from declarative config, there's a… there's an instrumentation Top-level element as kind of a wide-open thing for… Expressing whatever static configuration, so it doesn't obviously cover functions like request hook, but, to make available to instrumentations.
typically the divide there is… that I've seen people talking about is doing it per instrumentation, but there is an instrumentation.general area that tries to do general things, so… which I think aligns a little bit with what you're thinking. So there's an instrumentation.general.http.
hierarchy under there that one example is which client headers for HTTP requests to be capturing, and that would be… theoretically used by all instrumentations that are doing HTTP client-related things. There's another one for URL sanitization, so it's something that might cover the sanitize URL thing here, so that… There's something… about that on the other side. Sorry, go ahead.
**Jared Freeze** 10:05 And so, you said it doesn't support functions, though, so… is sanitation.
**Trent Mick** 10:09 Well, I mean, declarative… the declarative config does not… yeah, it can't, because it's a… modeled around a static YAML file.
And I don't think anyone's ever gonna get into, like, put some JavaScript code in your YAML file, and we're gonna eval it for you and do that, so… but yeah.
I just want to throw out that there is this idea of… in declarative config, but it's still in infancy as well, so I don't think it necessarily has to be a strong guide for what's done here, but there's an idea of having Configuration that's common for… What you're configuring, rather than specific to particular instrumentations.
That's it.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 10:53 So for us, would it make sense to have, like, a instrumentation section in the SDK configuration, but first, that would kind of mirror something like this.
**Trent Mick** 11:07 Yeah, maybe, that's… that's hard to… David and I are… Chatting about this earlier, and… do… And on the node side, we're bringing our hands, too, around configuration.
Cause the instrumentation is… somewhat of an afterthought are different, because the instrumentation is… passed to the function that starts the Node SDK are generally passed in already created, so their config has already been specified, so… Or you create some system similar to what, Auto Instrumentations Node has, where you don't create the instrumentations, you pass it in a factory so that you can collect configuration And then create the instrumentations with that config that's been passed into this start node SDK.
function, but yeah, so I don't… I don't know.
I don't think they… clear path is obvious, especially when you want to do, on the browser side, tree-shaking stuff. Like, you don't want to just accept a whole bunch of config, and it's like, oh… they specified some config for this instrumentation, so now I need to import that thing, and do I do dynamic import or not?
That creates… the problems. So, yeah, sorry, I don't really have a hard, strong opinion on what the right thing to do is here.
**Jared Freeze** 12:36 Okay, cool. Well, I guess, Yeah, we'll leave notes here, and… See if you can get a PR.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 12:45 I just, just really quick, I, related this, I guess, like, I tried to do something similar.
You know, a few weeks ago, by lifting the, the apply custom attributes callback to the SDK level.
Although we decided not to do that because… Because, you know, some instrumentations may be passing You know, their own custom context, but… Yeah, I had, like, a similar thought there.
**Jared Freeze** 13:13 Does it make sense to do both?
I mean, you might actually have something you want to just put anywhere else.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 13:19 Well, I think Trent was making a point there, that it's like we can just use, custom processor.
To handle… to handle something that applies to all instrumentations.
**Jared Freeze** 13:30 So this is something we run into at Embrace.
Where we used to. You know, we have been leveraging event name to filter In the process, or… how do… how do you guys do that?
Right, like, you only want it to apply to a certain kind of blog or stand or whatever.
Do you guys use event name?
**Rebecca He** 13:56 I've used instrumentation scope in the past.
But… A lot of the times, they're more, like, generic attributes that apply broadly, and I think what we decided last time is, like, the only reason you'd want the custom hook is that you want the object that the… Instrumentation is dealing with, right?
**Jared Freeze** 14:15 Inc.
Yeah, that was… that's right, yeah.
**Joaquín Díaz** 14:23 I think if we can figure out, like, a shared context within both XHR and Fetch, that would be the context of that hook.
But I don't know if there is some… Some extra thing that each of the instrumentations would want to send to the contacts.
like, I don't know, the XHR object, in case of XHR request.
Whatever other fetch stuff you get when you, patch the methods.
I guess if there is none… nothing that we care about, like, individually for each of these implementations, and we only care about, like, actual network context, like URL and body or whatever, then I think they can be shared. Otherwise, I'll probably suggest we have, different hooks.
**Jared Freeze** 15:18 Cool. Let's see, anything else on this?
Alright. Did anybody else have anything they want to go over?
**Rebecca He** 15:31 I have a really small idea. Someone said they were… out for the next 2 weeks, I'm also out, but then I was like, should we just have a section in the dock? At the top?
We're… we write it, so no one has to keep it in… Their heads.
**Jared Freeze** 15:46 Yeah, I mean, we could do that. I think Slack is fine, too. Like, I… I like the Slack, where it is, that's… You know.
That's fine, But yeah, I mean, if you want to make… you want to modify this, you're welcome to. This might be auto-generated.
**Rebecca He** 16:03 Yeah, I was just thinking a section above the meeting notes that's just, like, upcoming… Out.
Outages or whatever.
**Jared Freeze** 16:13 Yeah, seems… seems fine.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 16:18 Yeah, what I've seen people do, like, in the past, like, if it's just, like, one week yourways, then you just, like, add the next… just like in the, attendees for, like, the next week, you just noted that you're out, but… yeah, I mean, maybe this is better.
**Rebecca He** 16:37 When does… is there, like, a bot that produces the meeting notes?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 16:40 I got a loan.
**Rebecca He** 16:41 I'll mess with that.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 16:42 No, but you can create a new one if it's not there, it's fine.
**Rebecca He** 16:48 Cool.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 16:51 I also don't… I also… I mentioned it, but because I… I, run the meeting sometimes, so… but I don't know, so… You also don't have to, like… If you'd, you know…
**Rebecca He** 17:06 Yeah.
**Trent Mick** 17:07 The bot's called Martin, is what you're saying.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 17:11 Yeah.
**Jared Freeze** 17:17 Okay, well, I guess I do have, like, two other little things. One's not ready, but I'll put it on the radar, is that instrumentation base.
I was thinking about redefining for Browser, so we're not pulling in Node, because it does kind of screw up the editors.
The editors are not aware that we need to be looking in browser folders, because they don't deal with package JSON.
It's just a… it's a rough idea. I'll… I can send it out next week.
And then the other thing is, it's, we're getting close. So, September 1st?
Actually, this is probably Trent's announcement, really, but there's a code Freeze.
happening, and I will be working on the build system for core. So, it's been ongoing, I mentioned it already, but I'll be working strictly on that, and I… would really love people to be doing QA at that point, so… I'll make sure to post links, and I was gonna find out if we have any kind of… Anything that'll auto-public, like, to a branch.
If not, I will… tar it up and send it to whoever's willing to install it, so…
**Trent Mick** 18:36 Yeah, we still have to work on it. The release tooling in Quora for similar, for the same.
Everybody saw branches, yeah.
**Jared Freeze** 18:43 Yeah.
Martin, you want to talk about this one?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 18:50 The sum con… yeah. I mentioned it last week, The PR has been open for about a week.
Just a… just a reminder, if you haven't seen it, please take a look and… And either… either approve or make comments, so we can get this going.
Yeah, thanks, thanks, Jared, for the review. I'll follow up on that.
**Jared Freeze** 19:18 Cool. Yeah, it was just… these, some of these reflect what's in TypeScript. That doesn't mean… it might be the other way around. We may want to change the code a little bit, and not that this may be correct for the required and recommended, so… Yeah, if you want to pair up on that, it'd probably be faster on Sun's bubble or something, so…
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 19:38 Okay, yeah.
**Trent Mick** 19:42 And then would you generate a package from this?
As well, to have, like, the constants defined similar to the semantic conventions.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 19:51 We would definitely generate the constants in some way, yeah.
I don't know, like, if it… not… probably not a separate package, but…
**Trent Mick** 20:02 Oh, like a subpart of the existing browser, where the packages are.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 20:06 Yeah, I think.
**Trent Mick** 20:07 I don't know, instrumentations want to import this thing, too, sometimes, so that's why it's a… it's an independent package with no dependencies on the… OpenTelemetry.js, so… Anyway, whatever. Sorry, I'm getting ahead of myself if you guys work on this.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 20:19 Yeah.
**Trent Mick** 20:20 Yes.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 20:21 So we'll still be, like, using the package that you publish from the JS. So, like, for the stable conventions that come from the course semantic conventions registry, we will still use that semantic conventions dependency.
But for anything… Here, what we would… Additionally, generate constants.
Okay, yeah.
**Trent Mick** 20:44 there's a… maybe related or something to look at then, if you want to, is there's a draft PR on OpenTelemetry.js for doing… GenAI-specific semantic conventions, because there's this conventions-gen AI repo that has their own federated semantic conventions, so… If you get to that point where you want to generate it.
A separate package, you could look at that PR, or how it's set up, scripts and things, but…
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 21:10 Yeah, that's useful. I think I was also looking at… I was also looking at the Android SDK they already have.
That it's not… Yeah, they already have that too.
**Trent Mick** 21:20 Okay, cool.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 21:21 Yeah, and this… this is just getting started, too. That's the… client instrumentation SIG that's, that's meeting on Tuesdays, every other week, so… The idea of this repo is to, Work on some… some other conventions that, are… shared between, or common between, or different client SDKs, so, like, mobile and browser, Okay.
**Trent Mick** 21:53 There was talk in the maintainer SIG earlier this week about having a short-lived SIG just for sessions. Did you hear about that?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 22:03 Yes. Yes.
**Trent Mick** 22:06 So that's potentially interesting to people here.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 22:08 Yeah, I actually mentioned it last… in last week's meeting.
**Trent Mick** 22:12 Okay, okay.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 22:12 Something that we would like to get started in.
**Trent Mick** 22:20 Alright.
**Jared Freeze** 22:22 Cool.
Anybody else?
Okay, all good. We can wrap up here. Thanks, everybody.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 22:37 Thanks, Pleasure.
Just really quick, let's do a release. I think, David, you wanted to do a release. The PR is approved, but it does need to, you know… whoever merges it, merges it can't publish, so you need to coordinate with somebody else.
**David Luna Bistuer** 22:55 Okay.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 22:56 But we can, we can do it now, right after this meeting.
**David Luna Bistuer** 22:59 Okay. Yes, I can… oh.
**Jared Freeze** 23:01 I can approve.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 23:02 Cool, alright. Thanks, everyone. Bye.
**David Luna Bistuer** 23:05 Thank you.
