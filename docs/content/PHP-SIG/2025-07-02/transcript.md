SIG: PHP SIG
Date: 2025-07-02
Duration: 62 minutes
============================================================

## Zoom Recording Transcript

Chris Lightfoot-Wild 00:00:12 Hey, Brett?
Okay.
Oops.
Not sure. I could hear you. Hello!
brett 00:00:43 I'll be back.
Chris Lightfoot-Wild 00:00:44 Oh, I can! I just heard it.
brett 00:00:46 Oh, what happened?
Good! I was just about to shut everything down here and start it up. That's good.
Yeah.
Chris Lightfoot-Wild 00:01:01 We'll just breathe for a little bit.
I wasn't sure given. There's only 2 of us. If it was my side or yours, so.
brett 00:01:07 I wasn't sure if well, I wasn't frozen on my screen, and you weren't frozen on yours. So how do we know.
Chris Lightfoot-Wild 00:01:16 Hopefully, we get a 3rd party to come on.
Confirm.
brett 00:01:20 Yeah. No bob. Today.
Chris Lightfoot-Wild 00:01:24 Yeah, enjoying the what's no doubt very hot weather in Georgia, I imagine.
brett 00:01:28 Yeah, is it normal to get a take a week off for the 4th of July? Or is it just a.
Chris Lightfoot-Wild 00:01:34 I think we did it last year, didn't I? As well.
brett 00:01:37 So high.
Chris Lightfoot-Wild 00:01:39 I'm not sure they don't get that many days, do they? To play around with over there so.
brett 00:01:42 True. True, we take take the long weekend while you've got it, and extend it for all it's worth.
Chris Lightfoot-Wild 00:01:52 It's understand that we're a bit spoiled in the Uk. But.
brett 00:01:56 In terms of sort of oh, do you call them Bank Holidays?
Chris Lightfoot-Wild 00:02:01 Well, yeah, we get Bank holidays. But then, like just regular holidays as well. So we get about 20 holidays a year, 28 days holiday.
brett 00:02:08 28. It's pretty good.
Chris Lightfoot-Wild 00:02:11 Yeah, so that's all standard. And so then you can have more. I only work a 4 day week. So there's an extra 50 on there.
Yeah. Fantastic.
Yeah.
brett 00:02:21 Hello, Sean!
Shawn Maddock 00:02:23 Hello!
Chris Lightfoot-Wild 00:02:24 Initial.
Oh, maybe not. Set the agenda
brett 00:03:02 Hello, Argo! Hello, Sergey.
Ago Allikmaa 00:03:04 I.
Chris Lightfoot-Wild 00:03:06 No.
Sergey 00:03:07 Okay.
Chris Lightfoot-Wild 00:03:11 Brett, were you against if I tag that discussion point onto the agenda
brett 00:03:16 No, no, not at all.
Chris Lightfoot-Wild 00:03:19 Let's work.
brett 00:03:20 Haven't thought about it a lot myself, but worth
yeah, no, no problem at all.
Chris Lightfoot-Wild 00:03:29 Thank you.
Pawel Filipczak 00:03:42 Hey, guys.
brett 00:03:43 Hello, Powell!
Chris! How do you feel about screen sharing.
Chris Lightfoot-Wild 00:04:32 Yeah, that's fine. No problem. I'll send it through.
brett 00:04:36 Thank you.
Chris Lightfoot-Wild 00:04:40 So they wanna take anyone else away from it if they want to do it. But not
You're already taking the the attendance there, Brett.
brett 00:05:06 No. Actually, I just guessed couple of hours ago goes pretty close, though.
Chris Lightfoot-Wild 00:05:17 Is that everyone? Oh, I go!
brett 00:05:20 Okay. Largo.
Chris Lightfoot-Wild 00:05:23 Do you? Do you wanna add him in? My, thank you.
Let's see.
Sorry it's not that fun on a single screen when there's all the overlay zoom components everywhere, just trying to move them out of the way.
Can everyone see? Okay, yeah.
brett 00:06:07 I can.
Ago Allikmaa 00:06:08 Yes.
Chris Lightfoot-Wild 00:06:10 Oh, and of course I have just in some of them
pause, screen, sharing accidentally somehow.
Second.
cool so go through, I guess
what? Prs, we might have initially.
No, anything you wanted to talk about that already, Brett.
brett 00:06:51 not really. Simcom should be a pretty easy one to review. There's barely anything for us. I'm just trying to keep up up to date they're up to. They've just released 1, 35. So
just trying to. Yeah get them all get them all done.
I don't think there's anything else from me? Oh, there is. I've reopened the way down the bottom.
Remove event logger. I think I finally got that got that ready?
Or I revisited that the other day. So that's that's ready for for a view, please.
Chris Lightfoot-Wild 00:07:33 That's cool.
Shawn Maddock 00:07:36 That related to the conversation we had in slack a couple of weeks ago.
Where I think you were saying, in addition to span events going away.
The event, logger, whole construct is going away, and they're just moving to logging events as log.
brett 00:07:58 Yes, yes, that's the one.
So the event log has been deprecated for for a while, probably since January. I probably did those at the same time. And it's it's removed from spec.
Yes. So it's working through how to
remove it from as many places as we can without breaking things.
Chris Lightfoot-Wild 00:08:29 Thank you.
Issues on here. Anything nothing in the last couple of days. But anything
on here that you want to talk about Brett or Sean.
all good.
brett 00:08:48 No, no, nothing, nothing from me!
Shawn Maddock 00:08:53 Nothing this week.
Chris Lightfoot-Wild 00:08:57 Sorry you you were okay as well.
Shawn Maddock 00:09:00 Yeah, I'm good.
Chris Lightfoot-Wild 00:09:02 Thank you.
A contribut. Then pay as we've got here.
You've got one, Brett.
Is that one ready for review? I'm guessing.
brett 00:09:12 It is. Yep.
Chris Lightfoot-Wild 00:09:14 Trying to take a look at some of these, maybe this evening.
And then let's say, for that instrumentation, no issues or not.
I didn't go through the stats or anything on the
brett 00:09:38 So they haven't changed much since last week.
Chris Lightfoot-Wild 00:09:44 Nothing new on stock overflow. But I'll just ticked off
Ops project bots
anything jumping out here that I don't want you to discuss on anything in progress
brett 00:10:11 You look 1638.
Is that being done.
or is it just the Apis? Like? Sorry the interfaces that have been moved?
No, that's right, my mistake. So this must be a 2 part up, because I know that the a couple of Apis for component providers have moved.
Sorry interfaces have moved into the Api. So this must be talking about moving some other
actual components into into the Api, so has not been done.
Chris Lightfoot-Wild 00:11:03 Sorry I muted myself. I'm guessing on the back of this. Neva was happy for us to pick it up ad hoc, so.
brett 00:11:14 Yeah, yeah, I think if he was
going to work on it, and imminently, he would have just submitted a Pr.
Chris Lightfoot-Wild 00:11:32 This SDK dot env one I've got that draft Pr. Still, but that's in. You'd
We'll have some comments on again this week, last few days.
brett 00:11:43 Yeah, yeah, I just. I'd forgotten about it for a while. But I saw Nivey mentioned it
just randomly in some other issue which reminded me to go back and have a look at it. So
yes, yes, yeah.
Chris Lightfoot-Wild 00:11:58 I can answer your outstanding questions, but I guess then
would you be happy for it to go in initially, then, with maybe the proposed changes, or some of the other proposed things happening down the line.
Just.
But there's
the provider for that environment. And Php, any whatever is kind of duplicated by the package as well as
the SDK.
And.
brett 00:12:25 Hmm.
Chris Lightfoot-Wild 00:12:26 I I guess it would just be good to
pull them together at some point.
brett 00:12:32 Yeah. Yeah. Yeah. We could probably do that in in 2 stages, though.
Introduce, introduce the new, and then I see you in update what we have now to
to use this environment loader.
Chris Lightfoot-Wild 00:12:50 Yeah, I just. I wasn't sure if
was the existence of that package, just because it was kind of proposed functionality at some point. But actually.
if we're if we're adopting all of the way it loads its components, then
that is just absorbed into the SDK,
and is no longer necessary as a standalone package.
brett 00:13:11 Oh, do you mean the SDK config package.
Chris Lightfoot-Wild 00:13:15 Yeah, a lot of what that provides is that not?
Is there gonna be a clear separation of the 2? Or is that gonna be just provided by the SDK.
Calls for the future.
brett 00:13:26 Yeah, okay, well, let's I think it can eventually make its way into the into the SDK,
I think we just need to.
Yeah. It's gonna take work, I think, because it's just it's got dependencies on everything. And it's gonna really break out. You know, the Api
shouldn't depend on anything below it, and the SDK shouldn't blah blah so to to do that. Well, just be
yeah. We'll just. We'll just take some work to sort of fix those those Api issues dependency issues. Sorry.
Chris Lightfoot-Wild 00:14:05 Yeah, no, that's all good. I just I wondered what the rationale was. But if
if that's what, if that makes sense, then all good.
Sergey 00:14:12 Can I? Just
verification? Question is, the purpose of this issue is to essentially load Laravel's end and use it as configuration for the SDK itself.
Chris Lightfoot-Wild 00:14:24 This was quite a reliable issue, but like more generally, to have Dot env support.
Symphony's got a package, and the view.
Sergey 00:14:35 Okay, so not not necessarily for Laravel. So like, if if other frameworks have other mechanisms, because it sounds to me like it will be a little bit of chicken and egg, right? You need to configure SDK to even enable instrumentation.
But if you're saying it's not about, it's gonna be kind of like universal thing. It's more about like end file. And you would just want to add
and file file support to SDK without without any relation to lateral itself, like, even if later, will have additional ways to configure it. SDK will not pick it up right? It's not the purpose of this issue.
brett 00:15:07 That's right. It's just just to layout
environment, variable input or variable input from a dot env file.
Shawn Maddock 00:15:16 Right, and the purpose of the.
Sergey 00:15:17 So.
Shawn Maddock 00:15:17 Config package just to abstract all that right? So that.
like you can specify it, and then a dot, inv or
command line or config, file, or whatever, and the individual components don't care. They're just reading.
Is there a config for.
brett 00:15:36 This value.
Yes, although it hasn't come up yet, whether the config file should consider dot env files.
But yes, the config we're talking about the declarative config file. Is that right?
Yeah, cool.
Yeah. Yes, it is meant to sort of.
I guess, be it be an alternative to environment based configuration
and also provides a much richer
experience. Because it's so much more descriptive.
You know you can fit a lot more. You can write a lot more in a yaml file than you can in a handful of environment. Variables.
Sergey 00:16:20 A couple of questions so just to understand. So it will be universal, not necessarily related to Laravel in the sense. The reason I'm asking is not because of the end file itself. It seems to be a convention probably shared by almost all the frameworks, but, for example, there might be some settings there that are specific to Laravel, like, for example, application, name, or however they call it.
and technically it should be mapped into the service name from hotel point of view, right? It's kind of like really similar concepts.
But in order to do that, we need to know that it's laudable right, unless we automatically, essentially, what I'm asking is, is, do we plan in some way be aware of
meaning of that of those options? And maybe there will be some mapping required.
or we will just take them as they are, and.
brett 00:17:07 No, I don't. I don't think so, Sergey, and, like the the open telemetry spec is clear about where service name should come from.
and there are. There's 1 variable. There's 1 way to do it. We're we're really just supporting, being able to define that in a dot env file.
Sergey 00:17:28 Right, right.
brett 00:17:29 It sounds good.
Sergey 00:17:30 Sounds good, sounds good, sounds good, so like simplified at this point. And the second question like, How How will you determine the location of this file, like SDK itself? Is it aware what is considered to be like root of the application, or whatever.
Chris Lightfoot-Wild 00:17:44 It is using. But yeah, from the composer installed version
path that gets from the packaged up.
Sergey 00:17:53 Okay, so it will somehow.
relative to the location of the Comp. Of the SDK package itself. It will determine, like it will assume that it's inside some kind of vendor folder, and then it will calculate relative to that what is considered to be a root of application.
Chris Lightfoot-Wild 00:18:09 Yeah. So I think there's already a get route path, or something like that in installed
gives you the best of the app with them. I think it goes.
Sergey 00:18:17 The reason I'm asking those questions is because in our case we separate right? We bring SDK outside of application. So for us, it's it's completely like that's why it's jumped to me like how we even can find what is where the application is located.
But
Chris Lightfoot-Wild 00:18:34 That lives outside of the dot envy. So then you could give it a base path or something like that.
Maybe that was something we'd have to look into to accommodate.
Sergey 00:18:51 Sorry. Maybe I misunderstood. Are you saying that you will allow people to configure where the env file is located?
Chris Lightfoot-Wild 00:18:57 Well, that's what I was just, I guess. Propose or asking, is that something that you'd see? It.
Sergey 00:19:03 That will definitely work. But I I thought, you you guys want to make it automatic as possible, right? Discover where it is. So we're just wondering how this discovery will work.
brett 00:19:13 At the moment is that it's just. It's at the root of of your application. And so.
Sergey 00:19:19 I think it's
but since we we follow the concept and elastic distribution as we per site, right installation, then we immediately kind of become. It's in. It's more challenging because it's we can install SDK outside. It's not brought with the application itself.
So there might be multiple applications installed, and each of them will have its own inv right? So kind of like, when application starts in some way, we need to understand that application started. And we also need to determine where it's located, but I guess it can be done. I guess.
If we assume that application always comes with the
with vendor, for with the composer, then we can see where composer invokes
vendor or folder. And then relative to that decide. Okay, that's that's the location application. I assume. Probably some like wordpress is still gonna be a challenge. But
I know if N. File is relevant to wordpress.
So maybe it's a combination that is not interesting.
Chris Lightfoot-Wild 00:20:16 Yeah, maybe that's something we could expand after this one lance and see
see how it feels. I guess.
Sergey 00:20:24 And the second question I wanted to ask. So you guys mentioned that it's gonna replace the content of N file is gonna be, only it gonna be considered. Or are you guys considering like laying, laying multiple sources and then giving them priorities and finding each option which what is the highest level priority source that you can find it in. But if it's not there, then you go to the, you know, to the lower level, and so on like, is it gonna be layered configuration sources, or is gonna be just always one.
brett 00:20:53 Layered. Yes, so the way it works now is it'll check the environment, and then Php, dot any, and then
a dot env provider, if if if there is one available so if I understand.
Sergey 00:21:10 So dotting, we will have the lowest priority, so it only will be. It will be only be used, fallen, fallen out only if those previous 2 sources don't contain the explicit definition explicit setting for that option.
brett 00:21:22 I think that's how it currently works. Yeah, as hmm.
I was just reviewing it yesterday. So it's still sort of fresh
in my mind. Does that sound right to you, Chris?
Chris Lightfoot-Wild 00:21:33 Yeah, I think so.
Sergey 00:21:35 Assumed the other way around like ends should have the highest priority, since it's per application.
But maybe I'm missing. Like environmentals can be defined on system level.
So they will have kind of like more global
into that. But maybe maybe there are different.
Chris Lightfoot-Wild 00:21:52 We'll check into that as well, because I'm a bit rusty on that Pr. Even though I did it but a few months. Well, I'll try and move.
brett 00:21:58 It's a good quick. It's a really good question. And yeah, maybe, Chris, just take a note to.
Pawel Filipczak 00:22:04 I agree with Sergey. So now we we was implementing the OP. Pump for the for our distribution.
and the OP. Is is the highest priority, because he it can override what what was set on the system right? Because in other cases it doesn't make any sense. So I think the same is with the the 10 fives.
Sergey 00:22:27 It was worth considering, like what other deployments like. Is it possible that people would prefer environments like it sounds to me
the Monaro, the the location should have high priority, right? Because then it will allow people like, for example, some people don't have any control, like, for example, or any file, because it's it's installed by system administrator. So they cannot even change anything that comes from it. So they but end file. They can probably place with the application, so it will allow them to override whatever it is in. If we want to to allow them to do that right sounds like we. We should allow that.
Yeah.
brett 00:23:04 That that makes sense that yes, you could be more specific per application by giving a a local
dot in file a higher priority. I I see the point. I think it's a good one, and worth considering.
Shawn Maddock 00:23:23 Surprised.
The spec doesn't specify which order.
brett 00:23:29 Talks about M. Files at all. I think we've just done it as a bonus.
Gotcha.
Sergey 00:23:34 Talk about multiple sources of configuration like this whole layering concept? Does it mention that.
brett 00:23:40 No, not at all.
No, it's it's just environment. It either comes from the environment or declarative config. And so we've
gone. We've expanded at that to allow Php, dot any, because
I can't remember why someone suggested that would be a good idea once upon a time. And dot inv, because it's really common in sort of, I guess symphony and laravel and a couple of really popular frameworks is that's just how everyone operates. So we should try and
sort of support that.
Sergey 00:24:18 Makes sense.
Chris Lightfoot-Wild 00:24:21 So on on the back of that the preference will be dot env, because it's the most likely to be specific to the the app.
and and then fall back to server and sorry. Emv, and then.in a sort of
what's the last one.
brett 00:24:37 Yeah. It's a good question.
Sergey 00:24:40 Some people, I think, prefer that any, because I think it's easier for them like environment, like, for example, if you run in the context of a service like Fpm. If it starts as a demon, it's very hard to set environment variables for it, like
as maybe in its configuration.
I assume in order to decide on those things, you need to consider like, what is the deployment model? Right? What what is the easier for the application level people to change like without having administrative privileges on those hosts that probably should have higher priority. Right? Whatever people with less privileges can change.
they should have higher priority than when you need root to change something
like set environment variables on on demons that probably should have the lowest priority.
Chris Lightfoot-Wild 00:25:28 So you'd think.mv in the environment.
Sergey 00:25:33 I think we all agree that that image should be on the top, like be considered first.st Now, the decision between environment and Ini file.
That's interesting. Question I I don't even remember what we did in classic.
Hey, Paul, do you remember what we did for the E dot like, or do we even do that with any.
Pawel Filipczak 00:25:53 The Nfl. Is over the I. 9.
Sergey 00:25:56 So environment has higher priority. So we consider environment 1st and then AI.
Pawel Filipczak 00:26:01 Yes.
give, give me one sec. Are you checking the code now? I'm I'm not sure but.
Sergey 00:26:10 Yeah, worth considering, like, definitely, yeah.
Chris Lightfoot-Wild 00:26:23 anything else on this
project, Bob, before I close it off.
Pawel Filipczak 00:26:29 Oh, yeah, I have a. I have a response for several questions. So yeah, 1st is a pump dynamic config, then I 9, and then M.
So Aina is over.
Sergey 00:26:41 I had some support cases asking us. No, I think a pump will be on top even above the 10, because it's kind of like the dynamic thing that can change.
Pawel Filipczak 00:26:50 During the lifetime of the process.
Sergey 00:26:53 Yeah.
Pawel Filipczak 00:26:55 So the purity of pump. Then Ini then enth.
Chris Lightfoot-Wild 00:27:02 Yeah, yeah. And then worship on in dot. Nvin.
Sergey 00:27:05 Yeah, I think you put it the right that yes.
brett 00:27:08 I think I think that's what we just agreed on that that.in would be.
And and as far as as your Pr. Is concerned, OP-amp is not
in the picture, because that's something that applies afterwards. But as far as initial configuration goes.
Pawel Filipczak 00:27:25 Think that? Am I? Am I right in saying that.
brett 00:27:28 Like that. A service wouldn't get its initial configuration from OP. Amp. OP. Amp.
Sergey 00:27:33 Currently it depends on the timing like, since we do it in the background, if it will be fast enough before even the 1st request comes in, so I guess it's the time in between module in it, right, Pabel, and the requesting it like if it will be fast enough
to to fetch on the phone.
Pawel Filipczak 00:27:49 You know, I was testing with a very basic cli application. Right? So it's it's the there was really basic application. Just you know, some Eho or something like that.
So I received from the local collector, received configuration faster than php medialized. If we, finishing utilization of the all of the extensions. So from from the early beginning of the request, I got the 1st configuration. So we are not doing.
Sergey 00:28:17 But from timing point of view we will start to spend spawn the background, thread in module in it right, and we'll try to fetch it from the module in it, call right.
Pawel Filipczak 00:28:26 Yes, exactly exactly so it it's it's happening in the background. So it's it's fast enough. But it's not guaranteed that it will be before the 1st request.
Sergey 00:28:36 Yeah, we had discussions in our team about whether to block the application to guarantee that remote configuration is required before we even allow application to start, but that was teamed as not observability.
good behavior to start affecting application and blocking it
like. So, for now we unfortunately have this a little bit of a race in that sense that
we don't know. Maybe a couple of big requests at the beginning. We'll use local configuration, not the.
And I will not be affected by remote configuration.
Shawn Maddock 00:29:10 We move this to a
get issued, just so that whatever decision gets made is documented, and all the rationale behind it.
Chris Lightfoot-Wild 00:29:20 Yeah.
Sergey 00:29:22 Are you referring to this dot env discussion, or Pam.
Shawn Maddock 00:29:28 Config Priorities.
Sergey 00:29:30 Hmm.
yeah, I I assume discussion about our pump will be relevant. We'll bring them, and we will be contributing that. But yeah, both ends.
If you guys implemented, I agree that ports documented that.
brett 00:29:46 Feel like. That's something that the spec should probably
clarify if it doesn't, rather than the Php. Sig.
instead of deciding on what does the spec say if there is remote config available via OP. Amp, and.
Sergey 00:30:02 No, that's that is clear, you know. Pump. It says that it should have high priority over the local
that is clarified in opalm right?
Session.
Pawel Filipczak 00:30:12 Yes.
Sergey 00:30:13 Yeah. So the relation between local config and all pump is clear. But what what about the different sources that are local, that there? What is the priority between them? That is, I assume specific to Php. Might be.
brett 00:30:24 It is. Yes, yes, that makes sense. Yep.
Chris Lightfoot-Wild 00:30:30 Cool.
That's it.
Close this tab and then road to SDK to. There's a few bits and pieces on here, but so you've got some stuff.
Sergey 00:30:44 But, by the way, just smaller note, sorry for disturbing the flow, just to clarify the reason I'm asked about this mapping between app name for Laravil and service name is because Opm depends on the service name. So we didn't want to get in the situation. We have this chicken and egg issue right when we don't know how to discover service name
before we fetch remote configuration right? Because if we rely on a lot of the instrumentation to kick in before we even know what is the service name. So that's why this decision. What you mentioned, Brad, is a good thing for us, like we? Okay, we'll know that if service name is determined without even instrumentation is being loaded, then
that's going to be the service name, no matter what so has been loaded cannot change it after that.
Yeah. So that's at least simplifies that use case because essentially, it's possible to set different remote configuration for different services. So you can say so. That's why we need to send service name to remote to collector, to give us remote configuration.
brett 00:31:42 Got it? Yep.
Chris Lightfoot-Wild 00:31:47 Cool. Thank you. And then nothing on the road to SDK. V. 2. Right, Brett, that you wanted to.
brett 00:31:54 No, no! I have done a little bit of work on
SDK. 2 in the last couple of weeks, but still in progress.
Chris Lightfoot-Wild 00:32:02 Cool.
Thank you. Well, I guess we could move on to the agenda items. So sorry it's taken as a while to get to that point. But Paul, do you want to kick that off?
Pawel Filipczak 00:32:14 So, yeah, we I just wanted to announce that we finally created an issue with the proposal of of the contribution. So
you are waiting for comments and questions, and we'll be happy to answer.
And if you have any questions, please go ahead and then review the the the issue.
Yeah.
Chris Lightfoot-Wild 00:32:42 Oh, that's that's.
brett 00:32:43 I assume there's a whole process here that that we don't know about, although I don't know about.
yeah, I've sort of.
I mean. I saw that there was a process when, say, Ebpf
was was was donated, and
you know there was a period of time for people to go over the code and check it for quality and maintainability, or whatever.
I assume, something like that's going to be expected of of our Sig.
Do you know anything about what the next steps are. Paul.
Pawel Filipczak 00:33:19 So I had somewhere the the maybe. Are you sure on the on the slack document with the donation.
a path? How to how to proceed with that. But yeah, we just need to
to wait a bit to everyone to read that document.
And if
you know, I don't know how it how it? How it works from the from the open telemetry side. So
I have no idea.
But I guess that
at at some point someone will start asking questions. So that's that's that's the how, how, how it should work.
But yeah, it. It requires a code review. And
then before the contribution and before, and I guess, after approval, we need to, you know, remove the trademarks from the from the code base.
And yeah, and
I guess this issue will start the discussion if it aligns the the whole idea of open telemetry. So yeah, that's that's it. And is it really needed or not? So is it a
most like a stone
close to the head, to to the leg, or just, you know, something which will improve them. The the quality and and
and ease of use, of of open telemetry for the Php. But
but I don't know how how the process looks from the other side.
I I will share the doc. I found I close the tab now, and so I don't have the link.
But yeah, I I will share it on the on the slack. Okay.
brett 00:35:06 Okay.
Pawel Filipczak 00:35:06 Into the document too.
brett 00:35:08 I saw severance already sort of
taking a look at this, so I'm sure he will be in contact as our
as our sort of primary contact from the the Technical Committee.
Sergey 00:35:21 But I assume you're right, but definitely, probably somebody from that committee how it's called the Governance. Whoever deal with this issue they will probably reach out to you guys to maintainers of of the Sig. So then, if you need our commemoration, please let us know if we need to.
maybe together on the replies to that, to their questions, like, what Pavel just posed like, how will it integrate with the existing Sig project? Right? So that's a valid
discussed in the past. But if we need to clarify it, then we can work together on
build in the past how we plan to integrate it all together. Yeah, so.
Pawel Filipczak 00:35:58 I put the the link to this. Contribute donation. Guide on the chat, so please click in the chat, icon, and then you should.
and I will add it also to the document.
Chris Lightfoot-Wild 00:36:21 Oh, someone's on it already. Thank you.
Pawel Filipczak 00:36:24 Yeah.
Chris Lightfoot-Wild 00:36:28 Well, was there anything else on that point, then, or is that? Leave it that we'll have a read.
yeah, cool Brett, you're next on that.
brett 00:36:43 Yeah. Oh, just just quickly, though. Congratulations, Paul, on getting that far through the the donation process. It's taken taken a while, so I assume that it was a lot of hard work going on behind the scenes.
Well done.
Pawel Filipczak 00:36:57 Thank you.
brett 00:37:00 just a small one from me, because it's come up over the last couple of weeks. But I did finally let the Ibm Instana dev know that would accept their code. And it's being accepted and merged and released. And it's our problem now.
Well, hopefully, not. But
yeah, I I did try to make it clear that the onus was on them to sort of be keeping an eye on
an eye on things, and we can't be sort of chasing them up for for sort of issues and resolution. So that's done.
That was it for that one.
Chris Lightfoot-Wild 00:37:39 Cool. Thank you.
Sergey 00:37:41 Question regarding that, does it include any kind of tests that like, what is the indication? If we break something like if we change something that breaks it.
No, not not likely. There will be an indication. Okay.
brett 00:37:54 Yeah, it. It has some tests. Yes.
Okay, yeah. No, I don't know.
Sergey 00:38:01 Okay.
Thank you.
Chris Lightfoot-Wild 00:38:03 It was the same I've seen there was test, but didn't have any context to like what instiner even is. So
I guess as long as we ping them. If something should break, we'll pop up and fix it.
brett 00:38:18 Oh, that's right. And I mean, it's at, you know, version 0 point 1. So
move fast and break things. Yeah.
I mean, there's there's only a fairly simple, simple interface for for exporting. So you know, I don't think that we would easily break it from, you know, from our core code by by changing anything.
but yeah, but that that's that's my concern is, you know, accepting random improvements from the community.
Is, is that a good thing, and that's where we we would expect.
You know, the the Ibm developers to sort of review those those code changes
and and understand what the consequences are.
Sergey 00:39:07 Makes sense.
Chris Lightfoot-Wild 00:39:14 Cool if we still got time. Then I've got this last bit, but we'll try and make it quick.
We discussed about like the stability of things in the
well. I guess it's evolving from the spec, and how we've supported that in the Api and our SDK in the past.
I don't think, Brett Brett seen this briefly, and commented, that I think sometime Java had already done a similar approach with having a separate yeah, package for the unstable parts.
So kind of got a very tiny proof of concept with
that, you know, does nothing basically
other than introduces a sort of different namespace for experimental or other features.
but we, you know, we might be a bit down the line far down the line to consider this approach or not. But I didn't know if obviously in future things continue to evolve and we want to provide.
But more bleeding edge functionality.
Is it something that we could consider.
I don't know, Brett. You're probably better place to comment on this, but like the way that some of the components are wired in in the SDK. Would probably
probably depend on spi for the
optional package to register itself via some kind of config to say, I want to use this piece of additional functionality or something.
Shawn Maddock 00:40:51 Don't have a lot of it. Just something
I've been looking at for my day job is open feature. It's a feature flag toolkit.
I don't know if that would be useful here, but it would be nice if there was some sort of feature flag where we could just enable experimental features.
to gain access to all this, whether that's
whether it's a separate namespace or repo.
I think it's an implementation detail.
whether it's required or not. But yeah, it would be nice to be able to turn them off for stability, and to enable them for
for testing. In playing.
Chris Lightfoot-Wild 00:41:37 I I guess part of it is what if someone's extended
operating code explicitly of that? You know SDK component, that's got a different signature, and then we change it.
whereas at least, if you've had to
import a different namespace or something you kind of, it's there in the code that's experimental. But.
Shawn Maddock 00:41:58 Sure.
Chris Lightfoot-Wild 00:41:58 It's only conventional, is it? It doesn't actually mean anything. And
to someone that's using it, it might feel like it's broken. But
so I'm not. I'm not. I don't feel strongly about this. I just wondered if it was some kind of consideration or.
Sergey 00:42:16 Can you give an example like, what are the experimental features that you want to try to add like that?
brett 00:42:22 Really, it's basically anything that's in the spec as experimental. Because we
if we implement things when they're experimental, and then
you know what that means in the spec is subject to change or removal. And we
get into trouble if we deploy
these experimental features as if they were stable, and then people
depend on them, and then they change, or they go away, such as the event logger, which came up a while ago or earlier in this meeting
is, it is now very difficult to remove without breaking semantic versioning.
So yeah. And I. And I think that's where
java is a lot more cautious
than than we are, and all of these features live in a you know, a separate
I don't. I think they call it experimental or or something, you know, features
mature there until and and are tested out until such times they're marked as stable in the spec, and then they can move into the sort of the stable branch. So it's a it's a lot more complicated workflow. And I suppose that's my
my
fear looking at that is that it feels like more work for me and more things to think about.
But I I do. Yep.
Sergey 00:44:01 Yeah, sorry for interrupting. I, I, okay, I now, I understand. Okay, so there are certain aspects. So yeah, I I think most of the discussion here is about the Api of the SDK right? The Api
it is used by instrumentation stuff like that. So essentially, I see that there is, you can market with attribute. In this case it's older. This
I don't know.
And
should we use like already, this attributes in Php, right? But that doesn't matter. It's a technical thing. So let's say, we market like that. Is that not solution enough? Like, why do we need more than that? Is that by itself is not something that can be removed like if
if if it's made clear in documentation and in source code, that certain parts and features are experimental. I saw that you guys separated in separate package and stuff like that.
What does it by you having it in separate package, even though it sounds like it's not completely separatable, right? Because you still need the, you can separate interfaces, but you still need to implement them in the same classes that implement those interface right? So they will invade the SDK itself. You cannot have, like a separate package that will be called SDK. Unstable right? It still will be part of the SDK.
Chris Lightfoot-Wild 00:45:11 Well, that's what this would have done that like to split that out. And then, I guess subclass whatever interested so that in this example there was like a tracer that extended the existing SDK, one
Sergey 00:45:27 I see. So you're saying so. But what does it buy you this additional level of having them addition in separate packages, like the fact that people take need to take dependence on those packages, so it will make them clear that what they are doing can can change at any moment like just to drive that point home. Is that the purpose.
Shawn Maddock 00:45:47 It's really the semantic versioning, whether it's a breaking change or not, that
if we take something out, even if it was marked as experimental. It's technically a breaking change.
brett 00:46:00 It is technically, yeah, yeah. And the spec kind of
strongly encourages us to follow semantic
versioning, but also strongly encourages us to never
change, particularly the Api in a in a breaking way. Which we we can't
do. I think we certainly can't do
now like there, there are breaking changes that we've we're just gonna have to leave them as deprecated and leave them in.
yeah, yeah, I I don't know the answer.
Sergey 00:46:43 But I just wonder, like, what is the concrete. So I guess maybe I need to refine my question about the concrete use cases. Yeah, you're right. So we have all these experimental features in SDK, but the question is, what is the advice, then, for those people that write instrumentations like.
okay, they can use them, but they instead can be broken by any future version of the SDK. Because those features can go away now they still need, then they cannot rely on semantic version in of semantic conventions. Right? Because, okay, because experimental, it can go away, even though the version it should be compatible. So what then?
like, what do they get from this? This additional knowledge? Like, it sounds, I'm trying to understand, like, what is the what is the best practices that have been then proposed to the instrumentation authors?
How do they? Should they use this knowledge that something is experiment.
Chris Lightfoot-Wild 00:47:37 Well, I'd I'd like to think
that's where I go, Sean, you go first.st
Shawn Maddock 00:47:43 I mean to me it would be anything in the main repo or namespace
you can rely on and like in composer, you, you market with your
what is it the carrot to
say? Yes, I'm I'm good with this version, not worrying about it, and the unstable is always going to be a 0 dot something.
and we'll just increment that forever. 0 dot 1, 32
as we're playing with unstable features. And so if
really, if you're rating an app, and you want
to use those unstable or experimental features, you just know, like you got to stay on top of
every single update to see if
it's breaking your app, whereas if you just want to do an auto instrumentation package and forget about it, then only rely on
the features in the in the stable, in the main branch or not branch, but package.
Sergey 00:48:48 Oh, but technically so, we're talking about instrumentations that can be broken again with
people that will take those instrumentations and will use them. They don't understand all this thing that's going on inside them. Right? They don't. They will not see. Okay, this instrumentation took dependency on this as stable Api.
They just want to use this instrumentation. And okay, they upgrade the SDK to some next version and then suddenly breaks. By the way, I assume technically so. This will require also, I guess, to SDK also to be pinning the Api and stable version right? That it it depends on it cannot just use carrot for the for Api and stable. Right? So SDK and stable. We also have to PIN the Api version Api.
Chris Lightfoot-Wild 00:49:34 Yeah, it depends on. Yeah. It's a minimum.
Yep.
Sergey 00:49:41 No, I guess it. No minimum will not work, because otherwise it will rely on the semantic version. And and the fact that it's any minor version of also compatible. But it's not the case for the unstable.
So SDK unstable
package will have to PIN its dependency on the Api and stable to the particular version that it depends on right. It cannot just say.
and
but it's a technical thing. But I'm trying to again to bring it back to the end. User experience, like
the experience will be the same as it is now like.
So to those instrumentations that use unstable.
So it brings to me. I'm just trying to understand. What is this additional complexity? Advise us.
Okay, that makes easier to please. Go ahead.
Chris Lightfoot-Wild 00:50:27 Sorry I was. Gonna say, does it give the instrumentation author at least a choice of
stable, or take a risk that there's unstable like. In this particular example there is enabled method
would be deemed unstable. And as an instrumentation author, you might say, well, it's not in the stable, Api. I'm not using it.
That doesn't affect the the end user application. But the instrumentation also could
made that decision themselves, at least versus. Now, if the
we've just implemented it, and it's got an annotation that's experimental. It's still it kind of exists, and you can depend on the what looks like a stable Api, but it can change down the line. So it kind of. I guess it's more frustrating than that.
If you didn't really.
Sergey 00:51:12 It will make it more error, error, proof, like, if people didn't look at the that attribute didn't see it, or didn't even care to look. They just saw that there is an is enabled method. They just used it. You're saying now, it will be harder for them to just use it because they need to go and explicitly take dependency on Api and stable, and only then they will be able to use it. So that will. That is what we want.
Chris Lightfoot-Wild 00:51:35 Well, I I think you could still like go wrong with it. But the fact that you've had to kind of opt in to take that experimental or non stable dependency.
Those you kind of knew the steps you were taking to get this piece of functionality
right. My initial thought. I don't know. Brett like you've obviously said there's complications to this as well. And so maybe
you know, this could be something we just don't throw away. But I'm just thinking longer term as well if there's more and more to come
like the way. But we always.
Sergey 00:52:04 If understood, the Sean suggestion to move the check to the runtime instead of like
static time, like static analysis. There is no compilation time in HP,
but let's say, call it kind of compilation time, right? So this one allows you to discover earlier that you use something unstable. But if you move it to Runtime. Let's say you check at Runtime. If the option is not enabled to use experimental features, then it will just fail at Runtime. But I guess it only might depend on the on the you know, if your testing involves the those cases. So I agree that failing on the static time is better because you it's more deterministic.
The discovery that you use something unstable.
But yeah, so I wonder like how much overhead it will introduce because of this split that you now need to combine this 2 kind of like trees of stable and unstable
is that something that is can be easily done, or and then, when you need to bring it all together, it's a lot. It might be quite a lot of overhead to restructuring the code like that.
Chris Lightfoot-Wild 00:53:11 Do you have any thoughts on that, Brett? Because I've got a couple of.
brett 00:53:14 I, I do feel like it's gonna add a lot of complexity. And yeah, I I see that
the sort of the the safety argument, but also.
Sergey 00:53:31 But maybe it can be sold, for example, by some kind of like static analysis thing, like, for example.
HP stun or any of those tools they allow implementing plugins. Right? So maybe we can implement a plugin. They just will automatically detect all those usages like, if you didn't say explicitly in composer is an option that you want to use. Experiment will just fail and not allow you to pass static analysis. So, for example, I don't know how easy that is that to do.
But that's, for example, an option
like, if the question is only at which point is discovered.
Then maybe there are other tools that can be used, not without requiring this splitting code.
Shawn Maddock 00:54:13 That it's Php. Stan, or whatever, though, is kind of a dev requirement to hotel. I don't
know if we want to do that.
brett 00:54:23 Hmm true.
Chris Lightfoot-Wild 00:54:29 Cool. Okay.
brett 00:54:31 Yeah, I. Personally, I think I probably feel better about just marking things as experimental and saying semantic versioning
guarantees don't apply to things that are marked as experimental. I'm sorry your code broke.
Chris Lightfoot-Wild 00:54:47 Yeah, that works, too.
I mean, I'm on the like.
Sergey 00:54:52 Do you guys heard about from from instrumentation authors that
that would. It would have helped them like not to step into this thing, or is it just you think that it might be a good like?
I'm just wondering, like.
brett 00:55:07 Year.
Sergey 00:55:08 Is this a use case? That is, widespread.
brett 00:55:12 No, no, it's not. No, we're just trying to be very, very careful to not break other people's code.
Chris Lightfoot-Wild 00:55:24 There was always one queue in the past, wasn't there someone that was maybe frustrated, that something had changed.
brett 00:55:30 Oh, yeah, we've definitely had a very small number 1, 2, 3 people complaining that you know you changed an interface and it broke my thing. Please don't do that. Why did you do this in a.
Sergey 00:55:43 For example.
brett 00:55:44 Why, why wasn't semantic versioning fired.
Sergey 00:55:47 But, for example, the breakages that I'm aware, like when every time I upgrade the versions of instrumentations is the change in the attributes being used right? How data is.
brett 00:55:55 Thank you.
Sergey 00:55:55 Produced. So that sounds like this will not address that right? This change will still.
So I'm just wondering, like, if that's the most widespread use case when the end user is being broken. Right? Whatever you wrote to use an old data format like your dashboards, or whatever searches, or however use the data will stop working, because now the attributes different. So you will be broken anyway. So is it worth investing in some other use case? That is not even the most widespread one
they just
I'm I'm talking about my personal experience, right?
Those use cases that I encountered when something breaks.
even though it shouldn't, based on semantic version.
Shawn Maddock 00:56:41 I like the attribute or annotation is.
I don't know the next step. The next iteration of how we go about experimentalizing our code.
Sergey 00:56:58 But this attribute annotation. It's only for the developers to look at. Right? We're not gonna in any way automate anything based on it.
brett 00:57:06 I don't think so. It's just just a warning signal to to a developer.
Sergey 00:57:11 Right.
brett 00:57:17 Yeah. So we've got the I think we call it experimental php, doc, which we do use
fairly, extensively, and it covers
a lot of use cases.
Sergey 00:57:31 Do you know if it's possible to to even instruct, or some other static analysis tools that can fail if you use any of those marked with a particular Php Doc. Or attribute.
brett 00:57:43 I know depth track can cause. I happen to be looking at that today.
but I don't know that that helps. 3rd parties know if they.
Sergey 00:57:56 Yeah. But, for example, if you run that on the contribut right, at least, people when that want to push it into contribut will be immediately aware of that.
If you don't do them. If they don't run those checks in their environment, at least when they push those things into the repo. They immediately see that.
Shawn Maddock 00:58:17 I like that we can, having
sorry, didn't mean to talk over your.
brett 00:58:21 As I said we we could definitely I I think we could do that with depth track where we could say
I don't know at least warn or something. If if anything is relying on an experimental function or class.
Sergey 00:58:39 Yeah. And then we can discuss like, if we want some instrumentations to be using those, maybe then. And somehow, in in their composer, Json, or somewhere. They need to be, you know, in big letters declared, and then they will skip the check
or views, and they will be allowed to use. But then, at least, it will be clear to those that people that take
that take dependency on those instrumentations that this instrumentation is
will fail next SDK version, but possibly right.
brett 00:59:06 Hmm.
Sergey 00:59:07 It relies on experimental features. So be aware.
So maybe it's particular versions of I mean, I don't know if we want to get into parallel trees here, having experimental version of exhibition. So but
maybe the good start just to what you mentioned. If there is a tool like that just to flag.
Start with that and see if that is good enough for now.
And this simple solution that made others, you know, like 2020, 80 approach right?
20% effort that might address 80% of concerns.
And it'll be good enough for now.
Chris Lightfoot-Wild 01:00:03 Cool. I'm sure we can put that on the backlog as an issue.
Well, that's alright. We'll just post a quick action point there. But yeah, for further discussion.
brett 01:00:13 Yeah. Yeah. And then the onus is on us to, you know. Make sure that we do annotate
things as experimental.
The specs gotten a lot better recently about marking things as experimental, and you know, eventually stable
so we we should do that as well. And I think I think some of the
the problems we have now are sort of self
self caused because we treated things experimental features as as stable, or forgot to mark them as experimental or.
Sergey 01:00:55 I mean, technically, if it happens frequently, you can even for that implement, a tool. Right? For example, you have. We can have a tool that on Hpr. If it sees that you removed something, it will check if it was marked Experimental and flag it again.
if but we are going everyone further like, like, you know.
depends if you want to invest in those tools. And
but and you might argue that it will be too late anyway. Right you already. You already not marked it, but at least he maybe, if you will mark it, and then, you know, check it in, and then
we will have this 1st tool to discover if we have any of the instruments, but I guess it will have to retroactively do it. Yeah, so you you I guess you can. If this happens really frequently and you want to avoid it. You might solve with good tool. In some of those use cases.
brett 01:01:45 Yeah, I don't think it's a frequent frequent occurrence, but it's.
Sergey 01:01:49 Yeah, that's cool.
brett 01:01:51 So maybe difficult problem when it does come up, though.
Sergey 01:01:56 Yeah. So maybe I like you said, maybe it's 1st good enough to start with the, you know, being careful and doing it just following this practice. And
maybe it's not gonna be an issue anymore.
Chris Lightfoot-Wild 01:02:12 Cool. I think we're about time as well. Is there anything final bit? So we all good on that front.
brett 01:02:23 Well, good for me!
Sergey 01:02:24 I don't know. I guess we've reached the top of the hour or so. I just wanted to ask some small, but I I can add it to the next. It's not urgent. Yeah. So
I will. Led it to the next meeting.
Chris Lightfoot-Wild 01:02:36 Cool, alright. Well, thanks so much. Everyone see you next time.
brett 01:02:43 Thanks.
Cool. Goodbye.
