SIG: Kubernetes Operator SIG
Date: 2026-09-24
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Jerry Leung** 02:03 Hey, hello.
**Mikołaj Świątek** 02:05 Good… what time is it for you?
**Jerry Leung** 02:09 I am in Pacific time, so it is 9AM Pacific Time, which is good.
**Mikołaj Świątek** 02:16 Good morning!
**Jerry Leung** 02:17 Yeah, thanks. So, what time, what time in… Fuck you.
**Mikołaj Świątek** 02:23 I'm in Central European, so it's, 6pm.
**Jerry Leung** 02:27 Oh, not… not that bad.
**Mikołaj Świątek** 02:30 Not that, yeah, it's, it's… it's… I'm not gonna complain. I'm not gonna complain. It's often… it's often the case that we get, you know, around this time is when a lot of… most of Europe and most of the US can attend the meeting, at the very least, so it's kind of… Often.
Often like this.
**Jerry Leung** 02:55 Yeah.
sometimes… because sometimes… some meeting can be in very early morning or very late night, so I… so for PHP's sake, I have to attend, I think.
5 AM Pacific time, yeah, very early morning, so…
**Mikołaj Świątek** 03:14 Yeah, that's a… that's a sacro… that's a sacrifice for… for open source.
**Jerry Leung** 03:20 I,
**Mikołaj Świątek** 03:21 I would probably not do that. I would probably not attend this meeting.
**Jerry Leung** 03:25 Yeah, whoops.
**Mikołaj Świątek** 03:26 Sorry.
**Jerry Leung** 03:27 Yeah, same for me. So I… I attend when… when I am asked to… to attend, so, yeah.
**Mikołaj Świątek** 03:36 Alright, cool.
Now, we're gonna have to… my fellow maintainers are unfortunately chronically late, so we'll have to give them.
A few more… Minutes.
Are you, are you just, just, just so, so I'm not making, wrong assumptions, you're the author of the PHP Oscar instrumentation request, right?
**Jerry Leung** 04:14 Yes, yes.
**Mikołaj Świątek** 04:15 Okay, cool.
It's actually nice that you're here, because we'll probably… if anyone shows up… let me actually ping them.
Okay, so… Alright, I'm gonna give this 3 more minutes.
See, Jacob's not gonna be here, because he's… Dealing with an incident. Hey, Tyler.
I sometimes wonder, why are you… why are you labeled Rain Tank Incorporated?
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 05:16 This is how the company was founded under.
So, like, we're doing business as Grafana Labs.
**Mikołaj Świątek** 05:25 So it's a technical debt.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 05:27 Yeah. Maybe it'll change someday. Who knows? I don't… I don't understand the… filing rules for being a business in the United States.
Let alone, like, 20 other countries, since Grafana hires a lot of different places.
**Mikołaj Świątek** 05:53 Right, so for either of you who are not frequent, attendees of this meeting, I'm putting the… Running notes document link in the, in the chat.
Okay.
I wanna give… I wanna give Pavel and Benny a few more minutes to join.
Because there's… there are things to discuss, and if they don't want to show up and discuss, I'm just going to decide by my own.
with you, Tyler, acting as, you know…
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 06:28 I, I am, I have approval.
I have sub-maintainer levels of approval that we can use in time of crisis.
**Mikołaj Świątek** 06:36 You can, No, you, you can, you can try, you can try to stimmy my, my radical ideas.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 06:45 The radical idea of adding two new auto-instrumentations before V1 Beta-1?
**Mikołaj Świątek** 06:50 I don't think it's radical to add more to instrumentations, I think they're largely fine. It's more than just a question of how we're gonna… You know.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 07:00 I mean, to add any… to add any auto-instrumentation means messing with those… the deep, dark, horrible auto-instrumentation reconciliation logic.
That's all messy, that no one wants to refactor.
**Mikołaj Świątek** 07:13 No, it's fine, it's fine, but we'll get there. Yeah, I can see, I can see that it's only going to be us already. I don't know what it's… ABO is doing that we are unfortunately under, another second…
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 07:35 By the way, KubeCon, I just saw that KubeCon EU CFP is open. Anyone is interested in submitting.
I think it closes on, like, the 11th of October.
**Mikołaj Świątek** 08:09 Hot.
See if we're gonna get anyone else. We can actually, I think, start discussing the instrumentation, but this… I don't want to keep dragging Xuan here.
Waiting.
Right, so… We have Ruby as the simpler case, I think, of these two, because it's very straightforward, and it looks really similar to… to Python. It's even simpler, or maybe to… maybe even to Node.
And I don't see any reason in the Ruby PR to not accept it. Works perfectly fine to me.
it's another question of, like, you know, how to split it to merge it more easily. It's a different question, but I don't see… I think we should do it. It's just a question of… and this is… I think you might be better positioned.
to… to answer this? Tyler?
Because we have two options, right? We can merge it now, and then do… The migration?
migration.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 09:23 into the one beta one, you mean?
**Mikołaj Świątek** 09:24 Yes.
Yeah.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 09:26 I mean, V1 Beta 1 has had no traction.
Over the last… Four weeks, I feel like.
even my, like, image change hasn't really got through. So I think we keep… I think it's okay to add them in alpha.
the switch for these images to be required would be the same as every other image that would be required, so I don't think it's… an issue.
**Mikołaj Świątek** 09:53 kind of leaning towards that, though. Like, I would be leaning otherwise if we could give a concrete date.
Yeah, we…
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 10:03 I don't think we have any concrete date, especially because, like, Pablo's not even here, so…
**Mikołaj Świątek** 10:07 Yeah.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 10:08 Thank you.
**Mikołaj Świątek** 10:09 He's stuck in a different meeting, maybe he'll join.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 10:11 go.
**Mikołaj Świątek** 10:11 later.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 10:13 Do you know…
**Mikołaj Świątek** 10:14 Yeah.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 10:15 The one question that I know we've talked a lot about is… trying to rely on, like, the packaging SIG to deal with images instead of ourselves.
Despite the fact that we've added a lot of good tooling to make our own images better. Is Ruby in a place where we could… Put a hard line in the sand and say, no, we're not going to build yet another image.
Go work at the packaging SIG?
**Mikołaj Świątek** 10:42 you will be… you will be, gratified to hear that I've already obtained a, a promise on that. By the way, Xuan, am I pronouncing your name correctly?
**Xuan Cao** 10:59 Yeah, it's great.
**Mikołaj Świątek** 11:01 Alright, thank you. So, so, you're the, you're the offer of the Ruby, request, right?
**Xuan Cao** 11:09 Oh, yes.
**Mikołaj Świątek** 11:10 Yeah, so, is it, like, confirmed, confirmed that we… that we'll get the, the… the instrumentation image hosted somewhere by the Ruby SIG?
**Xuan Cao** 11:24 Yeah, well, we can host it. Yeah, the report I put on the comments, I will be the one to host this image.
**Mikołaj Świątek** 11:34 Okay.
**Xuan Cao** 11:34 But not the test image. I'm not sure if the test image should stay in the operator or not.
**Mikołaj Świątek** 11:41 Yeah, yeah, test it for the… because right now, remind me, do you have it in the pull request, or do you have it hosted on, like, your personal,
**Xuan Cao** 11:50 Oh, jutsu.
You mean for the testing image?
**Mikołaj Świątek** 11:54 Yes, yeah.
**Xuan Cao** 11:55 So, I don't think it's hosting anywhere, because, you can see the testing is failing, because it couldn't find the image, so I was just… also, I was gonna ask a question that how this… our process goes that were even merged, will the test image automatically, like, generated by the… by the CAICD workflow?
**Mikołaj Świątek** 12:16 The way… so, so, so it is, but there's, like, two tests that run it. There's, like, two, like, the test is run two ways. One is run against… The actual image in the repository as defined, and the other is run against, Oh, no, wait, we're talking about the test image, sorry. No, no, we actually have to merge it first. So what you have to do is you'll have to put up a pull request with just a test image. We're gonna merge it, and afterwards you'll be able to use it in your pull request proper, the instrumentation.
Okay?
**Xuan Cao** 12:55 Okay.
**Mikołaj Świątek** 12:57 Yeah, so… as you've heard Tyler, the Ruby SIG is going to host this image, so…
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 13:07 So, that's awesome. Would we need… So it'll be just like Go, then, where we don't have to keep anything in the, in the thing, and then… We would need a regular changelog entry when we bump that image.
Okay, sweet.
for the… for this PR, since it's pretty big, and it sounds like there are things in it that we don't actually need, like the… the Docker image, for example, I think there's a way… We could definitely break this into a smaller chunk by… First, adding… the code inside… Internal… internal instrumentation.
At minimum.
Nothing would be able to hit it, it would be there, we could unit test it, but nothing would hit it yet, so we could, like, merge that pretty safely, and then follow up with changes to the… changes to the API and the tests, and I think that would… that would be a pretty nice split to just not have a 3,000 line PR.
**Mikołaj Świątek** 14:11 I don't know, with these, I actually feel otherwise. Like, if I don't see the end-to-end tests passing, I don't actually believe that it works.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 14:22 Okay.
If you're… if you feel okay reviewing… I mean, it is kind of… Boilerplate from other… languages, but I know, like, for Go, for example, there was a lot of little… Strange nuances we had to do inside the… Inside the go dot.
goland.go, golang.go, whatever we call that file. So I guess the… probably the… all of the business logic is still held inside internal instrumentation, right? So that'll just be the thing to look at the most… like, look at closest.
**Mikołaj Świątek** 14:55 No.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 14:56 Okay.
**Mikołaj Świątek** 14:58 I don't know, like, we could try to split it, but I'm honestly not sure if, like, just reviewing the internal instrumentation logic is without seeing the context of the rest of it is really very useful. I personally, like, I don't really understand how this instrumentation works exactly, so for me, the proof that it actually works is the fact that the end-to-end test spikes.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 15:21 is the test. Okay. If you've already started reviews with the full thing, then we might as well continue.
I have not looked at this PR yet.
**Mikołaj Świątek** 15:31 Okay, cool. Yeah, so basically, the… where we stand is that… You can… you can put up a pull request with your test… with only your test image, and nothing else, just a test image definition and the publishing workflow for it, and we'll merge that.
And then, once you have your… once the actual instrumentation image is hosted with the Ruby SIG, then you put that in your actual pull request, and then it'll pass all the tests, and we'll be able to merge it. Does that make sense to you, Xuan?
**Xuan Cao** 16:05 Yes, yes, yeah, thanks.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 16:08 For the… for the test image… the test image is the… the app that gets instrumented, right? And we needed something to…
**Mikołaj Świątek** 16:15 Yes, sir.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 16:16 Are we going to be building that like… in its own workflow outside of any PR, and there's just, like, a test image that lives inside the operator's, like, package domain, or are we going to be building that on demand when it's time to run the test?
**Mikołaj Świątek** 16:33 The same way we do for all the other testing adjuster, like, actual… actually pushed to, like, to the operator GHCR, and just use main. Whenever you change anything in them, then the image is rebuilt, like, they're not complicated enough to, like…
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 16:50 Yeah.
**Mikołaj Świątek** 16:51 Make this more complicated, make this more complicated for ourselves.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 16:56 Okay.
**Mikołaj Świątek** 16:58 There is something of a question of whether, because we have the ability to make the instrumentations Enabled or disabled by default.
Via either operator configuration or command line flags and so on. And… Mmm… I guess this is maybe a question for you, Xuan, as well, what do you think? Whether we should disable it by default to begin with, and say that it's in beta, or some such, and then maybe enable it at some point in the future? I don't really have a great sense of how stable it is.
For example, just in terms of, like, the content of the image, and the semantic conventions, and so on, so… That's kind of my question as well. What do you think?
how it should go. Or should it just be enabled by default from the very start, and, you know, whoever wants to use it takes the risk?
**Xuan Cao** 17:54 Oh, I definitely think I should, like, disable by default, and then… I think that's how, like, all the, new features, like.
Represent by other… to others, like, the… Yeah, no, to be honest, I don't think it would be safe.
technology is stable.
That much, yeah, so… So, yeah, before I do that, like, turn it off by default, yeah.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 18:22 That's a little bit closer, too, to what we want in V1 Beta 1, also, where users have to opt in to using an instrumentation.
It's not exactly the same, because it still doesn't require you to force an image, it just requires you to set the feature flag, but… Or not the teacher flag, the command line flag.
But yeah, I liked that.
I'd like to opt in.
**Mikołaj Świątek** 18:44 So let's start with disabled, and, like, the question of whether… at which point it should actually become enabled by default is… we can decide separately.
In the future.
Right, cool, so I think that's… the Ruby instrumentation is covered.
Oh… I'll update the notes here, and now PHP. Alright.
like, my main reservation… you know what my main reservation is in that pull request, right? That mostly also looks fine, it's just that… the… the container cloning, I know that it's optional now, but, like, either… neither of those options are really nice. Like, the container… app container cloning to figure… this is for your context, Tyler, right? PHP is a little bit like… a little bit like the muzzle situation for Python and .NET in Overdrive. So there's, like, you need to know what things about the runtime in order to decide how to instrument it.
And here, here, like, Jerry is brave. He has this… he had this fun idea that you… to clone the application container and run, like, PHP version, something like that, inside to figure it out, which is… Definitely should be opt-in, in my opinion, doing something like that. But the alternative is to, again, just set everything in annotations, and that's also kind of… No doubt.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 20:21 That's what we did for .NET, right? We had people… in .NET, if you wanted to get Musil, you had to say, give me Musil, right?
**Mikołaj Świątek** 20:28 It's also the case in Python right now, but this is something the injector actually does solve, that the injector doesn't solve the PHP problem, and Michelle commented that it probably won't in the near future, because they don't like… they don't want to sniff on runtimes.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 20:45 Yeah.
So, I think… without having looked at the PR yet, my gut would say we should support that annotation method, but if we have a clever way.
to do it automatically, that an hotel operator… operator, like the person running it.
is acceptable, if they say that that's okay, then… I mean, that's nicer than having to split the annotation, but I… my guess is that we should have a fallback solution where that's, like, our existing pattern that's repeatable and knowable.
**Mikołaj Świątek** 21:24 I don't know, like, I think… I think it just… making a copy of the application container and running it is, like…
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 21:32 Oh.
**Mikołaj Świątek** 21:32 And it comes.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 21:32 The application container?
**Mikołaj Świątek** 21:34 Yes, yes, that's what happens in there.
That, that, that, to me, that's risky. Seems like a stickier.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 21:41 security risk.
**Mikołaj Świątek** 21:42 I know, you don't… you just don't… I don't know about security, like, you're running the same container that you already should be running, it's just that the…
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 21:50 Permissions and stuff.
**Mikołaj Świątek** 21:50 Absolutely.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 21:50 different, like… Yeah, like, running the container again under different permissions.
Because it would be under the operator's permissions, potentially?
**Mikołaj Świątek** 21:59 I mean, no, it's, it's, it's, like, it runs inside the same pod, with the same.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 22:05 Oh, okay, so it's just like another container in the pod?
**Mikołaj Świątek** 22:09 Yeah, but imagine somebody, like, eagerly running migrations in there or something, you know? You don't know what somebody's application has in their entry point.
Yeah. You don't, like, you don't know what's gonna happen. Like, theoretically, just running PHP version and making sure there's no entry point and so on, you know, that's probably okay.
But I wouldn't, like, stake my professional reputation on the probably.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 22:35 Is it something that… is this a feature that we have to have?
in our initial PHP offering, or is it okay to have the fallback annotation… or not the fallback, is it okay to start with the annotation solution that we use for Python and .NET, and then add this more complex solution In the future.
**Mikołaj Świątek** 22:54 I think this might be an easier way to get this in, I think. So, this is… feedback for you, Jerry, that if… if we could just cut out the container cloning and only keep the annotations, it's going to be easier to merge your request that way, and then we can later add the other option as, once this is in and it's, like, a little bit more settled. Does that make sense to you?
**Jerry Leung** 23:23 Okay, so I can… okay, oh, I think I could remove the clone… the app cloning logic, and keep the intonation for that, so… to keep the PR moving. And, yeah, for your information, I'm right now working with Mikola from the packaging SIG to see… to grinding the ELF header of PHP to see if I can get something from that one. If that works, then The entire logic can be in the injector, but… But I think, we are still grinding that, but we… we are not… we are not sure if we can do that or not, so, it may take some time, but sure, I… I would definitely remove that cloning… cloning part, and to make it… make it work and commit, to the… to the engine test first, yeah, sure.
**Mikołaj Świątek** 24:15 Okay, remind me, remind me, do you also have, like, a test application in there?
**Jerry Leung** 24:22 Yeah, I'm running a personal, fork of test app, so that all the tests can be passed. So, after the PR is merged, I will update to… to use the injector one. So, because Injector will also build a test app.
Okay. Yeah.
**Mikołaj Świątek** 24:41 Mmm…
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 24:42 I'm not sure what we do for .NET, I don't remember. Do we need to have… two test apps, or X number of test apps. Like, in .NET, we needed the MUSL and the lib… Something, something, something, one.
I'm fine.
**Mikołaj Świątek** 24:55 And we have, we have, we also have two for, like, the earliest and latest version that is… Okay, cool.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 25:03 So we… it would be good to have a similar testing strategy for PHP, since it sounds like… the PHP version is important.
And on the annotation discussion.
I think for, like.NET, we defaulted to 1.
I don't remember which one it was. Was it Lib?
G-something, libgc.
Or do we…
**Mikołaj Świątek** 25:26 Inc.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 25:26 justify it.
**Mikołaj Świątek** 25:27 It might be that we'll have to force it… force it to be specified, I think.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 25:33 Per PHP.
**Mikołaj Świątek** 25:35 Like, Jerry, what do you think? Like, for the annotation, do we… can we have defaults for the annotations, or do we have to force the user to set them and then just fail the webhook?
**Jerry Leung** 25:47 Right… right now, the, the platform, the… is… by default, the glibc, which is the same as other language, and for the thread safety, by default, I think it's for… it's the non-thread safety version, because PHP is natively single-threaded programming language. But for the PHP version, there's no default, because, it has to be set by user, so does that make sense?
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 26:19 If it has to be set, it has to be set. I think it would be nice to have a min and a max test of, like, this is a min version that our outer instrumentation supports, and this is the max version, and we have test apps for both of those versions in our end-to-end test. Check both of them.
**Mikołaj Świątek** 26:36 We'll have to… we'll need to document that, so… That's… as we… like we said for Ruby, it might be… It also might be easier to merge if we start off disabled, by default, in the operator. Like, the instrumentation starts off as disabled.
And you have to actually enable it via operator configuration, or via command line flag, before you can use it.
and yeah, you'll have to… you'll have to add documentation part, explaining, like, what the, what the instrument… sorry, what the annotations are, and that you have to set the PHP annotation, and if, like, if you don't set the… the user needs to know that if they don't set the PHP version annotation, it's not gonna do anything.
Right?
Because that's the only option we have here.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 27:36 They're sort of, is there, like, an event or some sort of information that we can… I don't know, record, like, hey, we found your annotation, but you were missing the version, therefore we didn't You can imagine.
**Mikołaj Świątek** 27:50 at an event, that's not a problem. We shouldn't fail the webhook, though. If you fail the webhook… Yeah, yeah, yeah.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 27:55 That's fine.
Yeah.
**Mikołaj Świątek** 27:58 So… so it should… we should emit, an event. You can also… set a status on the instrumentation, but that, like, if you want to set… do that for each pod, it just grows really quickly. So, like, emitting an event is probably the best way to… get, like… Diagnostic… That's what happened.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 28:21 Nevermind.
**Mikołaj Świątek** 28:26 And also, like, as just a general feedback to you, Jerry, because I see you're deleting the auto-instrumentation slash PHP in your pull request. That's really good, I am very in favor, but you can do that in a separate pull request, and I will, like, immediately approve it, and we'll merge it.
**Jerry Leung** 28:45 Okay. Sure.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 28:46 That'll clean up a lot of the scripting I just added for the changelog and for some of the other.
**Mikołaj Świątek** 28:51 That's one of the reasons, that's one of the reasons I want to get rid of it.
**Jerry Leung** 28:55 Sure, let's do that, because, yeah, the auto instrumentation image now is owned by, the PHP SIG, yeah. And, I think if… if the packaging idea is working by reading the EMF header, I could even remove that image in the PHP content and put everything into the packaging repository. But, yeah, it takes a long way to go.
**Mikołaj Świątek** 29:22 Yeah, the packaging segments are relatively new, so this is all, like…
**Jerry Leung** 29:28 In last, packaging sake, they agreed to host the auto-instrumentation package, the image, so, there's no need for PHP's SIG to own that, but it has to… I… I think we need to prove, that PHP can work with the packaging… packaging first, yeah.
**Mikołaj Świątek** 29:53 Yep.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 29:53 Do you think, Mikolaj, we could ever give away all of our test apps to the packaging SIG?
**Mikołaj Świątek** 29:58 I don't think we got them. If it was me, I would say no. I would say, like…
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 30:02 Right, so you're…
**Mikołaj Świątek** 30:03 Your testing is your own problem, Operator, so…
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 30:07 But it could be like, well, what if you want to test… I think there could be an argument made that's like, okay, well, the… inside the Java like, Agent SIG, they need a test app, and so, like, what if we all use the same test app all over the project? But, yeah.
**Mikołaj Świątek** 30:24 I mean, there is… there is hotel demo, but…
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 30:28 They're all already instrumented.
Or a lot of them are instrumented already, so…
**Mikołaj Świątek** 30:33 I mean, surely there's a way to disable it.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 30:36 Yeah, that's true. We could look into that. They're bigger, though. One of the advantages of ours is they're so small.
**Mikołaj Świątek** 30:42 fine. There's not really a big problem with our apps. The only big problem is that the .NET one is, like, some… sorry, the Java one is some weirdo, like, old thing that is annoying to update. That's basically it.
Anyway, so I think we are good. Do you… do you have any more questions, Jerry, about how this should go?
**Jerry Leung** 31:07 Yeah, I think I am good, yeah, so…
**Mikołaj Świątek** 31:13 Cool. So, yeah, since we decided we're going to merge this, like, we're not gonna make you wait for our, like, new version of the instrumentation CR, so we'll just, like, once… once these, like, things are cleared, we'll just… we're just gonna merge it.
And, that's gonna be it.
Thank you for being, by the way, so, so patient in pursuing this. I know it's been a long time.
**Jerry Leung** 31:37 Yes.
**Mikołaj Świątek** 31:40 Okay, so the other thing I want to talk about that is important is… I don't know if you're even aware of this, Tyler, but we have these feature gates for controlling network policies.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 31:52 Yeah, I'm aware in the fact that it broke the Helm track for a sec, but I just merged a bump, so I think Pavel fixed it, but I don't actually know what the…
**Mikołaj Świątek** 32:01 It breaks a great many things. It breaks.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 32:05 Is this a new CR? Is this a new CR for us?
**Mikołaj Świątek** 32:07 So, what it… there's, like, this is… there's two feature gates.
Alright? One of the feature gates just changes the default for the collector and target allocator CRs, and it… the default it changes is.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 32:22 it.
**Mikołaj Świątek** 32:22 Enables the network policy by default.
in them.
This is the less… I think we have, like, more issues about this open, but this is actually the less impactful one, because it's pretty easy to just disable it in the CR if you really want to. The bigger problem is that it also enables, by default, an operator feature, where the operator creates a network policy for itself.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 32:50 Okay.
**Mikołaj Świątek** 32:51 And why is this a problem? The problem is because all of the network policies put a limit on egress to the API server.
And the way they do it… is that they, go to the, default… there's a service in Kubernetes in the default namespace that has the API server, you know, API. So you go in there, you get the endpoints, and you put the endpoints in the network policy, right?
At startup.
Cool?
not cool. No, no, no, no, no, no, like, if we're… if we're on, like, EKS or something, these IPs can change over time.
Yeah, we've seen…
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 33:32 In Azure, we've seen problems with the KS attributes processor not being able to talk to the API, because it's, like, slightly different than an EKS versus GCP.
Yep. Okay.
**Mikołaj Świątek** 33:43 And also, there's apparently a whole bunch of problems where if you're running, like, a service mesh.
or your, like, your cluster is… has network… networking configured in some slightly… slightly spicy way, then you can, like… for example, those endpoints can be the wrong thing to go to, because you have, like, a local proxy.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 34:03 Because there's.
**Mikołaj Świątek** 34:04 API server on the node, right? So it actually should be a different… should be different IPs. And also, if you have Silium, apparently this is just impossible to configure normally.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 34:15 Well, that's service mesh for you. So, what was the original intent? So, like, why… it doesn't sound like network policies are useful at all. So, like, what was the original value?
**Mikołaj Świątek** 34:24 The original intent was to lock this down for security.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 34:27 Oh, okay, it's a period.
**Mikołaj Świątek** 34:28 basically it, like, that's what are network policies for? It's this, and I don't think original intent is wrong, exactly, it's just that we just severely underestimated the diversity of network configurations that exist out there. And there are, like, solutions to this. I opened… there's a new Pint issue, I opened it, I described what actually has to happen for this to be fixed.
But this is, like, a release blocker, and I don't want all of the, like, fixing it is not that simple. So, especially since there are, like, some… there's still discovery to be done, essentially. Like, we have, like, a bunch of issues from people with different setups, and it's not clear in some of them what we should even do, exactly.
But it's the.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 35:10 feature off by default?
**Mikołaj Świątek** 35:12 No, it's on by default.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 35:13 Oh, it's on by default, okay.
**Mikołaj Świątek** 35:15 And my… what I want to do is disable it.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 35:19 Yeah, I mean, it sounds like it… It sounds like it's not ready to be on by default, yeah.
**Mikołaj Świątek** 35:24 Yes. So that's… that's basically what I want to do.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 35:27 I mean, based on the Helm chart, I mean, this is, like, 2 months in, I feel like the Helm chart happened in August, and now there's, like, still issues. It feels like we should switch it back.
**Mikołaj Świątek** 35:36 Yeah, I think so as well.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 35:39 Which is fine, I mean, because I assume it's behind a feature gate, or feature gates, right? So switching it back to Alpha is a totally acceptable like, net flow of a feature gate, like, that's allowed, so…
**Mikołaj Świątek** 35:51 That's why it's behind feature gates. We just, like, switch it on. I think there's an argument even to… as to whether it should be enabled by default at all, ever, to be honest. But that's, like, a separate thing. I'm gonna argue with Pavel about this, eventually.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 36:08 Do you know… I don't know the intricacies of how this feature works.
But do you know… if we turn this off.
Is there a way to use, like, the concept of a network policy, like the network policy object, and, like, manage it yourself outside of the operator? And, like, throw it in front of the operator? Like, if I added something to the Helm chart, for example, that's, like.
You can create a network policy and just, like, copy and paste the entire object that you want, or something, like…
**Mikołaj Świątek** 36:36 I mean, you're gonna run… you can theoretically put whatever network policy you want in there, but you're gonna run into the same problem. You're gonna run into the fact that this is, like, in a network policy, you put an IP block, and this is not, like… in a lot of clusters, you don't know what that IP block should be.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 36:53 Yeah.
**Mikołaj Świątek** 36:54 Like, if you're running Silium, they tell you, don't use network policy, use psyllium.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 36:58 Yeah, because you couldn't use psyllium, yeah. Is the network policy only for communication with the operator, or are we also doing something where, like, the operator supports throwing a network policy in front of a reconciled collector?
**Mikołaj Świątek** 37:13 No, no, it affects the collector and the target allocator in that way as well, yes. They are also, like, restricted in how they can talk to the API server, which for the collector…
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 37:25 I mean, that is a cool feature, being able to say, hey, when I create my collector, throw this network policy in front of it, but yeah, if it's.
**Mikołaj Świątek** 37:31 I agree that it's very valid, like, you know, you can only talk to this, kind of idea in this respect, but… like I said, it's like, there's too much… I don't know, like, I didn't understand network policy as much as a feature, and now I think they're just kind of… Yeah, part.
It doesn't.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 37:55 It doesn't sound like it's something that we would ever want to have on by default. It sounds like it should always be, even when it's outside of the feature gate, it sounds like it needs to be an opt-in flag in the CR.
**Mikołaj Świątek** 38:05 Or it needs to be highly more configurable, or it needs to be highly more configurable and more permissive by default, essentially.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 38:11 Yeah.
**Mikołaj Świątek** 38:13 It's…
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 38:14 I mean, we… We don't… it's not like we deploy… the collectors that we create, it's not like we're using MTLS or anything with them by default, like, the things that we create are, like.
insecure by default, technically, right? I mean… If you want to add, layers of security in front of stuff is really personalizable.
I feel like it would be really hard to do that for a blank.
**Mikołaj Świątek** 38:39 I mean, honestly, like, you know, we always wanted to have a better abstraction for pointing instrumentations at collectors, and having MTLS in there, I think, would be a very valid feature for the operator to have.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 38:52 Sure, there's a good feature.
**Mikołaj Świątek** 38:53 with allocators.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 38:55 I just don't… I think it's hard to have it on… I think it's hard to have it on by default, but… I mean, we also have… I mean, the operator does kind of want Cert Manager to be there by default, and… there's… you have to take steps to not depend on the surf manager, so I don't know. But yeah, this thing doesn't feel ready to be on by default, the network policy stuff.
**Mikołaj Świątek** 39:15 I'm going to record that you agreed with me, and that we're going to do this.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 39:19 Yes.
it sounds like we've had several releases of… of trouble, and it's time to go back, and maybe… maybe it's just a matter of… more time to bake and get users to try it, maybe it's… we need a, like, significant amount of more testing. Like.
maybe some… well, it's hard to run platform tests in OpenTelemetry and all the different GCP, all the different.
**Mikołaj Świątek** 39:43 The problem with this feature, the big problem with this feature is that there's no way to… for us to validate.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 39:49 Yeah.
**Mikołaj Świątek** 39:50 rapidly.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 39:50 In the… in the KX Monitoring Helm Chart that I manage in… Grafana, we had… we were hitting problems like this, so we added platform tests for AWS, EK, like, GCP, Azure, all this stuff.
**Mikołaj Świątek** 40:03 Like, that's a lot longer.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 40:04 smarter to do.
**Mikołaj Świątek** 40:05 This wouldn't even work here. This wouldn't even work. You would deploy it on all of these platforms, and it would work.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 40:12 It would work.
**Mikołaj Świątek** 40:13 It would work, the problem is that over time, your IP addresses.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 40:19 You're in control.
So there's no, like, one-shot test, yeah.
Yeah.
I mean…
**Mikołaj Świątek** 40:26 It would, it would work.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 40:27 Best.
**Mikołaj Świątek** 40:28 psyllium, if we deployed it to, like, a psyllium cluster, we would know it doesn't work at all.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 40:31 Yeah.
**Mikołaj Świątek** 40:32 But, but, but for…
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 40:33 I feel like there's…
**Mikołaj Świątek** 40:34 York.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 40:35 There's gotta be some more community… discussion around the concept of, if we're hitting this problem, that means anyone using a network policy, just the generic Kubernetes object in EKS would probably be hitting this, so surely there's, like, a larger community discussion around this somewhere.
**Mikołaj Świątek** 40:52 I have consulted the clankers on this topic, and the clankers said that it is a known pain point.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 41:03 Okay.
**Mikołaj Świątek** 41:04 I don't know if that's true, but that was, like, you know… My… my… this was the extent of my, like, upower.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 41:12 Yeah.
**Mikołaj Świątek** 41:12 Essentially, I was like, surely there's a better way of doing this, right? And it was like, no, no, there's not.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 41:20 Yeah.
**Mikołaj Świątek** 41:21 Maybe, maybe it's another one of those, like, Helm… Helm's handling of CRDs kind of situation.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 41:27 Yeah, that's… at least Helm, like, has stuck to that very strongly. I still point to that… that ruling.
Pretty often. It's one of the reasons I try not to ever have to do CRDs, ever, if I can get away with it.
Because they're hard to manage.
It's great if you'd ever change the CRD, then everyone's happy. Never, ever break your CRD.
**Mikołaj Świątek** 41:53 No.
Alright, so that's all I had. I also had one topic which was, like, about, like, a release blocker that I want to get in, because this whole thing is also, like, made more complicated by the fact that Target Allocator has a bug where if you disable the network policy, it doesn't actually go away.
So you have to go and delete it manually. But that's already… Jacob already approved my pull request fixing this. Okay.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 42:21 If you do, like, the pull request to disable it, and you need an approval, just ping me.
**Mikołaj Świątek** 42:26 You know.
I mean, technically, I should wait for at least one major trip.
That's true.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 42:33 True. Do we have that rule here? We don't follow that rule on the collector.
**Mikołaj Świątek** 42:37 We have an informal rule.
We have an informal rule saying that depending on how, like, impactful whatever you're doing is, you should get, like, more maintainer approvals, but honestly, if… you know.
You know, people who don't review pull requests don't have a say in what happens. Yeah.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 43:02 That's me most of the time. I should review with more things, but it's hard to… it's hard to be all over the place.
**Mikołaj Świątek** 43:08 I know, I know the pain.
Anyway, so these are all the things I wanted to discuss.
I don't think there's any point in reviewing feature gate stability and issues to discuss at SIG. I've already pulled out everything.
There's one funny bit about the feature gate stability, but that's, like, an issue that Jacob can deal with on his own, I think.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 43:34 PR for adding, or making the image required does have approvals from all three maintainers. I think it's ready to merge, but also merging it doesn't really move anything forward. Not realistically. I need to talk with Pavel about, like, what his actual plan is, so I'll leave that up to you.
**Mikołaj Świątek** 43:52 What, like, because you can't merge it yourself, that's what you mean.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 43:57 Correct.
**Mikołaj Świątek** 43:58 I would imagine for you right now, then.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 44:01 Okay.
**Mikołaj Świątek** 44:01 problem.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 44:08 once the, once the PHP Actually, whoever updates the PHP folder, whoever deletes that PHP folder will have to do a little bit of scripting updating.
But it should be quite easy to take out the… The exclude logic from the changelog script.
It's all written in Go, so hopefully it's easier to look through than Bash as well.
I'm really glad we had the decision, Mikolaj, to go with Go instead of… 500 lines of bash.
**Mikołaj Świątek** 44:39 I find… I find that I do that more and more often nowadays.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 44:43 Yeah, yeah, we're doing it too.
Go or Python for anything that's, like.
Once you hit the 100-line bash limit, I've started switching scripts to something else.
**Mikołaj Świątek** 44:56 Yeah, like, but you also can overdo it and have a whole, like, multi-thousand-line package of tools in your repository.
Which is, you know, it's better to have a couple thousand lines of code than a couple thousand lines of bash.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 45:14 Once you do that, then you do the trick that the collector SIG did, where we move our Go tools into its own repository, and then it feels… then it feels better. Doesn't feel like you're importing thousands of lines of Go code, you're just importing changelog… changelog gen, or multi-model.
**Mikołaj Świątek** 45:30 Yeah, but then you have to deal with the release, the release ceremonies of a whole new repository, with the versioning.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 45:37 I know.
**Mikołaj Świątek** 45:38 That's really hard. All the tooling on top of tooling on top of tooling on top of tooling.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 45:42 Cooling, untooling, on tooling.
**Mikołaj Świątek** 45:44 Yes, yes, I recently… I got linked to this, you know, we have… the collector-builder, and apparently Google wrote a tool for managing multiple collector-builder, like, manifests.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 45:57 Great.
Right? Great and happy.
tool for helping with the collector builder, yeah.
**Mikołaj Świątek** 46:02 Yeah, so it's a tool on top of the tool on top of.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 46:04 Go on top of the tool.
**Mikołaj Świątek** 46:05 tool, yeah.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 46:06 Alec's been spending, like, the last two weeks trying to fix our Git workflows, and, like, we have shared workflows in OTEL now, so it's like, well, you can't just do it in… Contrib, you gotta go put it in shared workflow, and then go put it all the different places that could… yeah.
Tool management is its own… Job.
**Mikołaj Świątek** 46:24 Isn't I… I thought the coding agents would honestly help with that, but in practice, they, like, make it much easier to write even more bespoke tooling.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 46:33 Yeah, yeah, definitely. They just like… they're not good at going and finding an existing tool. They'd rather just write another 150 lines in a second.
**Mikołaj Świątek** 46:44 Alright, so… anyway, that's all I had. Thank you for helping me out, Tyler. I've been abandoned by my fellow maintainers. They are claiming they have stuff like, like, family, or, or incidents, or uncidents, right?
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 47:01 Another meeting.
**Mikołaj Świątek** 47:02 Yeah, yeah.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 47:03 We'll prod everyone at, we'll prod everyone at, at KubeCon.
**Mikołaj Świątek** 47:08 Yeah, I am definitely attending, by the way. I haven't.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 47:12 Well, yes, I am officially attending now.
**Mikołaj Świątek** 47:14 Yeah, I'm booking, I'm booking my flight, later this evening.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 47:20 I… I'm booked for Monday to Friday. I haven't decided if I'll switch to Monday to Thursday. There's… there's, like, a really good direct flight from Salt Lake City to Colorado Springs Thursday evening.
That I might… that I might switch to instead of doing a Friday morning flight.
**Mikołaj Świątek** 47:37 I, I basically, I basically have no choice if I want to do anything at all on Thursday.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 47:44 Oh, you, like, you have to leave Thursday, you have to leave Friday?
**Mikołaj Świątek** 47:47 Well, it's more like, if I… if I leave on Thursday, then it has to be at, like, 10 AM or something.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 47:54 Oh, okay, yeah, yeah, yeah, so you missed the whole day. Yeah, so might as well just go on Friday.
**Mikołaj Świątek** 48:01 I have to go, like, on a double, double transfer through LAX into Paris, into… into Warsaw.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 48:11 What?
**Mikołaj Świątek** 48:12 What do you mean, what? It's transplant.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 48:14 Why would it… I guess I wouldn't expect you to fly to LAX to fly back to Europe. I would have expected to go from Salt Lake City to Denver to Europe, or Salt Lake City to,
**Mikołaj Świątek** 48:25 - damn.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 48:27 That is inefficient. Not useful.
Or, like, or like Salt Lake City to Chicago? Yeah.
Bummer.
**Mikołaj Świątek** 48:38 Alright, anyway, we're… we're done. Thank you, Jerry and Xuan, for… for attending, as well. We'll, you know, we'll keep your stuff, we'll keep your stuff going. We'll try to get it merged for… for, like, the next two weeks, ideally, I hope.
And thank you.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 48:56 Yeah, and ping me when… ping me on those PRs, Mikolaj, and I can help review, since I'm familiar with the instrumentation logic in the… the… operator.
**Mikołaj Świątek** 49:07 I am… I am, in fact, adding you as reviewer as we speak.
I guess that's not enough. I guess I also have to, like, ping you on Slack with the link.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 49:17 Yes. Well, I need pinged when to take action, because otherwise I'll just ignore… I get too many GitHub notifications, so… I've done better now that I'm at a new job where I can keep track of, like, Collector and Helm chart, but… Then there's more things that it's harder to keep track of.
**Mikołaj Świątek** 49:35 Yeah, well, for you guys, Jerry and Xuan, see, Tyler is here, he's Tyler Helmuth on Slack, if you, if you want, want so, if you, if you know.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 49:44 Yeah.
**Mikołaj Świątek** 49:44 If you want to review your pull requests, you can just ping him, he just… he just agreed to it.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 49:50 Yep, that is true, I did do that.
Alright, thank you.
**Mikołaj Świątek** 49:57 Thank you. Have a nice rest of your day, or evening. See you.
**Xuan Cao** 50:00 Thank you.
