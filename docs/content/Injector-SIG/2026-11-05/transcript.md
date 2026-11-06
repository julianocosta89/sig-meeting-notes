SIG: Injector SIG
Date: 2026-11-05
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Nikola Grcevski @ Grafana / OpenTelemetry** 01:26 Hey, Basti, how are you doing?
**Bastian Krol (Dash0 Inc.)** 01:31 Hey, I'm fine, how are you?
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:34 Alright.
We're almost end of the week, huh?
**Bastian Krol (Dash0 Inc.)** 01:41 Right.
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:47 Just, updating the agenda.
I'm gonna put the same, I think, on the agenda, I think I just need reviews. Just wanted to see.
**Bastian Krol (Dash0 Inc.)** 02:10 Yeah, I've seen you, you and Nikola have been… Nikola Grcevski @ Grafana / OpenTelemetry 02:13 Yeah.
**Bastian Krol (Dash0 Inc.)** 02:13 See, you in particular with… Doing some archaeology on… JVMs? JVMs. That sounds horrible.
**Nikola Grcevski @ Grafana / OpenTelemetry** 02:25 It's horrible, and… But I don't know what else to do.
No, we just drop it, don't we just say.
Yeah, I don't know, like…
**Bastian Krol (Dash0 Inc.)** 02:36 I think at some point, we probably have to make a cut and say, yeah, that's… that we don't… the… Behavior is completely non-deterministic on something from before.
**Nikola Grcevski @ Grafana / OpenTelemetry** 02:47 Yeah, funny.
**Bastian Krol (Dash0 Inc.)** 02:50 And we don't make guarantees, I think that's… Nikola Grcevski @ Grafana / OpenTelemetry 02:52 They don't make guarantees, yeah, yeah.
**Bastian Krol (Dash0 Inc.)** 02:54 I think that that's… For me, that sounds, like, absolutely acceptable.
**Nikola Grcevski @ Grafana / OpenTelemetry** 03:00 Yeah.
I don't know how many we'll hit in practice.
**Bastian Krol (Dash0 Inc.)** 03:04 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 03:05 That will have this kind of problem, and are we adding complexity for no reason?
**Bastian Krol (Dash0 Inc.)** 03:13 I mean, what would the, like, like, just from the perspective of making that change now, what would… have been the behavior before, we would have injected unconditionally into any… so… whatever we do, it's definitely already a giant improvement, so… Nikola Grcevski @ Grafana / OpenTelemetry 03:32 Yes, yeah, yeah, yeah.
Yeah, it's true, it's true. And as long as you have the option to disable this, so… By putting the minimum version of zero, so… it's fine.
If people hit problems, we can easily tell them how to work around.
Yep.
Yeah, okay. Well, I got one approval, I just wanted to see if Nikola is okay with it as well, just to see if we just ask for another review.
Yeah, we fixed all the issues for last week, so… yeah.
**Bastian Krol (Dash0 Inc.)** 04:03 Yeah, sorry, I've not been really following along or doing a review, I was so busy with other stuff, and… Nikola Grcevski @ Grafana / OpenTelemetry 04:11 I understand, yeah. Life, yeah.
Work.
No, here's Michele I.
**Michele Mancioppi (Dash0 Inc.)** 04:18 Hello, hello. Antoine is chickening out today.
It may be only us.
**Bastian Krol (Dash0 Inc.)** 04:25 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 04:28 Yeah, here's Diego, and I don't know, maybe Jack will join, or did Jack bail as well?
**Diego Hurtado (Dash0)** 04:33 Ayyy.
**Michele Mancioppi (Dash0 Inc.)** 04:35 It was not unpacking.
**Bastian Krol (Dash0 Inc.)** 04:35 There you go.
**Diego Hurtado (Dash0)** 04:37 a…
**Michele Mancioppi (Dash0 Inc.)** 04:39 By the way, I'm happy to report that we had some very happy design decisions in the Injector.
By having the path for the, registration script.
are being configurable.
Because it so happens that the node people broke… That's.
**Nikola Grcevski @ Grafana / OpenTelemetry** 05:03 Excuse me.
**Michele Mancioppi (Dash0 Inc.)** 05:03 Keep on registering.
**Bastian Krol (Dash0 Inc.)** 05:06 Oh.
**Nikola Grcevski @ Grafana / OpenTelemetry** 05:07 Huh.
**Bastian Krol (Dash0 Inc.)** 05:08 What's up.
**Michele Mancioppi (Dash0 Inc.)** 05:08 I thought it broke the injectors out there, but it's not true.
So we can fix this in packaging for now, and then use it as an excuse for… to sit down and formalize the injection contract once and for all.
**Bastian Krol (Dash0 Inc.)** 05:23 Yeah, I mean, it will… I mean, outside of packaging, it will break Injector installations if people are unaware, right?
Oh, I see.
**Nikola Grcevski @ Grafana / OpenTelemetry** 05:32 It all just come through, I didn't pay attention. What the hell?
**Michele Mancioppi (Dash0 Inc.)** 05:35 That is, that is the reason why, Basti, we are in the digital operator, we're making, images that work in lockstep with the operator version.
**Nikola Grcevski @ Grafana / OpenTelemetry** 05:44 Let's have a coffee.
**Michele Mancioppi (Dash0 Inc.)** 05:45 Consistent installation, remember?
**Bastian Krol (Dash0 Inc.)** 05:47 No, no, sure, I mean, in the operator, we put it under different paths, Anyway… This…
**Michele Mancioppi (Dash0 Inc.)** 05:55 Normally.
**Bastian Krol (Dash0 Inc.)** 05:56 Not that pass, Sigment, you're right, that is fixed.
**Michele Mancioppi (Dash0 Inc.)** 05:59 If the OpenTele operator Had been using… No, even what they want to do right now, by putting the injector in every image that they inject that still would have been atomical enough not to break.
Which is cool. Folks, we did a good job. Nobody died yet.
**Bastian Krol (Dash0 Inc.)** 06:21 Awesome! Awesome. Yes. Yes, yes.
**Michele Mancioppi (Dash0 Inc.)** 06:27 Let's look at the PRs. Here we cannot have our weekly skit of asking Antoine what's going on with that.
I regret that. In reality, also, somebody committed, Nikola, on, putting QEMO under that.
**Nikola Grcevski @ Grafana / OpenTelemetry** 06:51 Yeah, I haven't actually done anything there.
**Bastian Krol (Dash0 Inc.)** 06:53 I mean, you have been very busy with the JVM versions, Stop, so… That's a very good excuse.
**Nikola Grcevski @ Grafana / OpenTelemetry** 07:02 Yes.
**Michele Mancioppi (Dash0 Inc.)** 07:02 has 55,000 commits.
**Nikola Grcevski @ Grafana / OpenTelemetry** 07:05 I know, but this ended up being more complicated than I imagined, so…
**Michele Mancioppi (Dash0 Inc.)** 07:11 Yes.
**Nikola Grcevski @ Grafana / OpenTelemetry** 07:12 Thanks for doing all the work, Michele and Bev.
**Michele Mancioppi (Dash0 Inc.)** 07:16 I hope you don't mind that I started out.
**Nikola Grcevski @ Grafana / OpenTelemetry** 07:18 Oh, no, that's exactly enough.
That's all great, that's why I have my branches unlocked, you can push to them.
No problem.
**Michele Mancioppi (Dash0 Inc.)** 07:26 This is my last thing from my side, then I would, I would plus one it.
**Nikola Grcevski @ Grafana / OpenTelemetry** 07:32 Yeah, I was just thinking, like, I think… I think it's good as info, man, because I… Because if it's… If we put in a debug.
I don't know, I think we run with our… correct me if I'm wrong, but I think we run with error log level by.
**Bastian Krol (Dash0 Inc.)** 07:48 Yes. Only error messages are… Nikola Grcevski @ Grafana / OpenTelemetry 07:50 Only I don't know.
**Bastian Krol (Dash0 Inc.)** 07:51 So, the line between war and info and debug is a little bit blurry, because I'm not sure how many people will set a custom debug… a custom lock level.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:01 Worko.
**Bastian Krol (Dash0 Inc.)** 08:02 Yeah.
**Michele Mancioppi (Dash0 Inc.)** 08:03 It's more like, Injector, tell me if you're not doing it and why or not.
It's, we might have over-engineered the log levels here.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:11 Yeah, so the question is, should we make a… so right now, we log that we didn't… we rejected instrumenting a process, like this one.
With info. So the question is, what do I make it?
Maybe we should make an error.
**Michele Mancioppi (Dash0 Inc.)** 08:30 If it's already info, then I'm pressing the merge button right now.
It was good. It was, it was debugged.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:38 No, no, it's… debug, it goes much more detail about why, but info is, This one is when he says, sorry, but we won't do it.
**Bastian Krol (Dash0 Inc.)** 08:48 I think we have a couple of other… cases already, so I could look for consistency, but whatever. So, I mean, like.
and we cannot find the or identify the lip C, then it's… also not an error, I think, but whatever.
Awesome!
**Nikola Grcevski @ Grafana / OpenTelemetry** 09:09 Right? Jesus.
**Bastian Krol (Dash0 Inc.)** 09:10 learned.
**Michele Mancioppi (Dash0 Inc.)** 09:12 This one,
**Bastian Krol (Dash0 Inc.)** 09:14 Bye.
**Michele Mancioppi (Dash0 Inc.)** 09:15 I'm not a PHP expert.
I, like the way it works.
Turns out that there is a distro, in, upstream that has the loader I wanted.
And I didn't know it existed. There is, They're missing the support for ZTS, but I think I think… That because of the loader, the injector doesn't care.
So…
**Bastian Krol (Dash0 Inc.)** 09:47 Let's, let's say fatigue, right?
**Michele Mancioppi (Dash0 Inc.)** 09:49 This is… ZTS is, threat safety.
**Bastian Krol (Dash0 Inc.)** 09:53 Yeah, okay.
**Michele Mancioppi (Dash0 Inc.)** 09:55 So… I need to look at it again, probably on the plane to CubeCon, or back.
But I think we might have a civilized path to PHP injection support.
**Nikola Grcevski @ Grafana / OpenTelemetry** 10:13 Wow, that would be cool.
**Bastian Krol (Dash0 Inc.)** 10:14 Awesome.
**Michele Mancioppi (Dash0 Inc.)** 10:16 So… Nikola Grcevski @ Grafana / OpenTelemetry 10:16 That'd be awesome.
**Michele Mancioppi (Dash0 Inc.)** 10:17 It is remarkably simple. So the reason why it took me so long to get here is that I did not know that there was a distro with a loader. So the way that this works… Nikola Grcevski @ Grafana / OpenTelemetry 10:28 I mean?
**Michele Mancioppi (Dash0 Inc.)** 10:29 Is that…
**Bastian Krol (Dash0 Inc.)** 10:29 What do you… what distro are you talking about, a PHP distro, or what?
**Michele Mancioppi (Dash0 Inc.)** 10:35 Yes.
**Bastian Krol (Dash0 Inc.)** 10:36 Okay.
**Michele Mancioppi (Dash0 Inc.)** 10:37 I'm talking about, this bad boy.
**Nikola Grcevski @ Grafana / OpenTelemetry** 10:42 Oh, so there's OTELPHP distro. Is this OTEL published, or… yeah, right?
**Michele Mancioppi (Dash0 Inc.)** 10:48 And we even have different RPM packages that will need to be migrated over.
**Nikola Grcevski @ Grafana / OpenTelemetry** 10:54 Wow, okay.
**Michele Mancioppi (Dash0 Inc.)** 10:56 It's a remarkable, it is remarkable of the fact that despite, discussing packages, like, 50 times in the maintenance call.
I was not aware that this existed.
**Nikola Grcevski @ Grafana / OpenTelemetry** 11:10 Wow.
Oh, this is awesome.
**Bastian Krol (Dash0 Inc.)** 11:13 That speaks of the diversity and size of the hotel ecosystem.
**Michele Mancioppi (Dash0 Inc.)** 11:18 That's me too.
**Bastian Krol (Dash0 Inc.)** 11:19 food.
**Michele Mancioppi (Dash0 Inc.)** 11:19 Lack of activity of some maintainers in… Going to the maintainer call and actually listening to what is being spoken.
However, however, this being said, the injection contract is super simple. It is, it is a Python style, where the injector is responsible to put on a path a stage one in a step. In Python is the sitecustomize.py. In this case, it's, it's a file.
an ENI file. The ENI file… has a SIDE2 loader that is an extension. It's a system object.
And then the system object, there's a del open to load the actual Python distro. So it is our first three-stage injection.
**Bastian Krol (Dash0 Inc.)** 12:11 Why did you tell us this?
**Michele Mancioppi (Dash0 Inc.)** 12:14 Because, I…
**Bastian Krol (Dash0 Inc.)** 12:15 I'd rather not know.
**Nikola Grcevski @ Grafana / OpenTelemetry** 12:17 No!
**Michele Mancioppi (Dash0 Inc.)** 12:18 It's actually a very elegant system. Now, the problem is, it happens on every single request.
**Bastian Krol (Dash0 Inc.)** 12:23 Yeah, sphp does.
**Nikola Grcevski @ Grafana / OpenTelemetry** 12:26 Nope.
**Michele Mancioppi (Dash0 Inc.)** 12:27 Not every SAPI is like that.
**Bastian Krol (Dash0 Inc.)** 12:29 Yeah, yeah, I realize.
**Nikola Grcevski @ Grafana / OpenTelemetry** 12:31 What do you mean it happens on every request? It's gonna check to see if it… It gets initialized on every request?
**Michele Mancioppi (Dash0 Inc.)** 12:36 Yes, yes, yes. Yeah, because every, like, Python, in most SAPIs, the SAP is, like, the mode in which you run it, and there are, like, 4 or 5.
Normally, every time, like, Apache with mod.php signs a request down, then a new Python process is bootstrapped.
**Bastian Krol (Dash0 Inc.)** 12:54 new PHP process.
**Michele Mancioppi (Dash0 Inc.)** 12:56 It's completely independent from the rest. He loads everything. He loads libraries. Beautiful.
So this is more or less how it looks like.
And, no, not this one.
So, we add something to the PHP scanDr that loads an INI file. The INI file says, ZEND runtime, load this SO file. The SO file then loads another SO file, and that is the actual tracer.
**Nikola Grcevski @ Grafana / OpenTelemetry** 13:26 Right?
**Michele Mancioppi (Dash0 Inc.)** 13:27 So, I'll, try to get this, in shape.
I, would like as many eyes as possible of people trying to break it.
**Bastian Krol (Dash0 Inc.)** 13:40 What we would really need here, in addition to us looking at that, would be some people with PHP chops to take a good hard look.
**Michele Mancioppi (Dash0 Inc.)** 13:51 Correct, and this is why, I got, Jerry, he's from, SolarWinds, and this guy is actually from the PHP Distro SIG.
**Bastian Krol (Dash0 Inc.)** 14:02 Nice.
**Michele Mancioppi (Dash0 Inc.)** 14:02 And I wanted yesterday to go to the SIG and talk about it, but I couldn't. So either I catch them at KubeCon.
or I go the week after that.
Because this deserves to be formalized as a contract.
Right? Like, hey, the Injector will modify PHP in its scan, and then the distro does the rest.
I have an example of an internal.
**Bastian Krol (Dash0 Inc.)** 14:31 I didn't catch that part. What is the contract here?
**Michele Mancioppi (Dash0 Inc.)** 14:36 We, in the injector, prepend.
to the, PHPs in Iskandir.
allocation.
That is similar to what you do with Python underscore, with Python path.
**Bastian Krol (Dash0 Inc.)** 14:54 So you mean that it's a contract specifically between us and the PHP SIG?
Okay.
**Michele Mancioppi (Dash0 Inc.)** 15:02 it needs to be distro. Like, this is how you shall inject.
I actually have, a draft of… the contract.
And Basti, I'm gonna send it over to you with extreme, extreme prejudice.
ready to comment.
And then Matt, will, go and do the talking in the, in the JS SIG.
**Bastian Krol (Dash0 Inc.)** 15:30 Yeah, sounds great.
**Michele Mancioppi (Dash0 Inc.)** 15:34 So we are finally at a stage in our revolution where we actually are going to talk about formalizing What the Injector does and say, folks, you're not gonna change that shit now.
**Bastian Krol (Dash0 Inc.)** 15:45 So, what I'm hearing is these, basically detailed contracts with individual runtimes, or the distros for the individual runtimes? How does it relate to our plans for the more general contract, or these discussions about injectability that we wanted to do?
Basically, runtime… Or independent of runtimes.
**Michele Mancioppi (Dash0 Inc.)** 16:14 That is painfully proceeding.
And it starts getting green marks.
Jack, helped me out, like, at some point, I could not do this anymore, then he took over, and he's getting it over the edge.
So I think that this gets merged soon enough, and then we have the, the bases in the SPAC to go to the SIGS and say, yo, we need to agree on that. Because this is effectively a clause in the auto constitution that these contracts shall exist.
**Bastian Krol (Dash0 Inc.)** 16:43 Okay.
**Michele Mancioppi (Dash0 Inc.)** 16:45 By the way, I would like to point out that I am seeing some auto maintainers.
Did he not?
Put a plus one here.
I'm gonna… I'm gonna put it in the chat.
**Nikola Grcevski @ Grafana / OpenTelemetry** 17:03 I'll give it plus one right away.
I think I see it, if somebody tagged me, I just… So many things going on.
**Michele Mancioppi (Dash0 Inc.)** 17:19 That is cool.
This one… I have no idea what, what… Gregor is trying to do. So, I have a vague understanding of the extension mechanism of the Java agent.
But I never managed to make it work, so…
**Bastian Krol (Dash0 Inc.)** 17:44 briefly looked into that, I, I don't… also don't, don't really know what's, what's going on.
**Michele Mancioppi (Dash0 Inc.)** 17:50 Can pass, perhaps?
**Nikola Grcevski @ Grafana / OpenTelemetry** 17:51 Pass-through extension pass, Injector pin's toes.
process startup.
Right, I think these Java extensions is something that, He wants us to be able to Pass them down to the Java agent.
And we currently don't support that.
I think it's simple as that.
It will surpass additional extensions.
**Michele Mancioppi (Dash0 Inc.)** 18:21 I do not understand what is the… what is the meaning of this.
So… Why would you want to use a different variable?
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:31 Yeah, he was surpassing, So these Java extensions are apparently additions to the Java agent that are not enabled by default.
**Michele Mancioppi (Dash0 Inc.)** 18:43 Perfect.
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:44 So you can pass them down to OTO. So similarly to what we do with all the other, for example, resource attributes, he wants to be able to… Like, have some… global ones, that may be the… some, like, operator or controller in Kubernetes will pass down a specific extension.
But then the users could have overriding…
**Michele Mancioppi (Dash0 Inc.)** 19:07 It doesn't make a leak of sense to me, for two reasons.
**Nikola Grcevski @ Grafana / OpenTelemetry** 19:12 Okay.
**Michele Mancioppi (Dash0 Inc.)** 19:12 Bun.
We are not touching this environment variable. So whatever you give us, we keep, we keep doing. We don't touch anything.
**Nikola Grcevski @ Grafana / OpenTelemetry** 19:21 Right.
Correct.
**Michele Mancioppi (Dash0 Inc.)** 19:23 Why using a different variable that is injector-specific?
So, if anything, if anything, I would expect the request to having this as a configuration on file.
Like, I don't get this PR.
**Nikola Grcevski @ Grafana / OpenTelemetry** 19:39 So, look, I think it's very similar to the Rezo's attributes, right?
Somebody could be setting in a script their own resource attribute.
**Michele Mancioppi (Dash0 Inc.)** 19:50 Yeah.
Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 19:51 And then… but you want to pass down additional resource attributes. Yeah.
from your operator.
Yeah. That say something else, right? So the injector will try to combine them together.
the hotel resource attributes, and the Injector resource attributes. So this is very similar to that. It's saying not just resource attributes, but also extensions.
**Michele Mancioppi (Dash0 Inc.)** 20:17 He wants this.
**Nikola Grcevski @ Grafana / OpenTelemetry** 20:20 Yes.
**Michele Mancioppi (Dash0 Inc.)** 20:22 Okay, I was profoundly trolled by the fact that there is no injector in the name.
**Nikola Grcevski @ Grafana / OpenTelemetry** 20:27 No, there is, because we allow for… Making sure that this, we don't clobber whatever they have.
**Michele Mancioppi (Dash0 Inc.)** 20:36 Okay, I misread it. Okay.
But then, okay, why this instead of this?
**Nikola Grcevski @ Grafana / OpenTelemetry** 20:46 Alright, that is a bad choice, probably.
**Michele Mancioppi (Dash0 Inc.)** 20:55 Because that is what confused the heck out of me. Like, I… I didn't.
**Nikola Grcevski @ Grafana / OpenTelemetry** 20:59 Right, right.
**Michele Mancioppi (Dash0 Inc.)** 21:00 is that Injector was there. It's like, why did the Java injection power.
**Nikola Grcevski @ Grafana / OpenTelemetry** 21:03 Right, right.
**Michele Mancioppi (Dash0 Inc.)** 21:03 Different.
**Nikola Grcevski @ Grafana / OpenTelemetry** 21:04 That's probably a mistake on his part, yeah.
Should be extensions there.
Yeah.
Yeah, exactly.
**Bastian Krol (Dash0 Inc.)** 21:16 I think you mean end, not end, and not end now.
**Nikola Grcevski @ Grafana / OpenTelemetry** 21:20 All right, and not, mister, yeah.
**Michele Mancioppi (Dash0 Inc.)** 21:22 Yes, thank you.
**Nikola Grcevski @ Grafana / OpenTelemetry** 21:47 Yeah, that's good.
**Michele Mancioppi (Dash0 Inc.)** 21:49 for the rest is… now that I get it, yeah, it makes sense to me.
Thank you for explaining. Like, I was looking at this, like, for half an hour, and it was not Thank you.
**Nikola Grcevski @ Grafana / OpenTelemetry** 22:04 Yeah, yeah, why is he doing that? Yeah.
I didn't know these extensions existed as well, I don't know.
**Michele Mancioppi (Dash0 Inc.)** 22:11 I have tried to make them work several times, and remarkably failed in every single occasion.
**Nikola Grcevski @ Grafana / OpenTelemetry** 22:18 Cool.
**Michele Mancioppi (Dash0 Inc.)** 22:20 Like, I failed so hard at that, it became a meme.
Add structure codes, so this is the one for Jack, which I think is a great idea, but needs to be rebased.
**Nikola Grcevski @ Grafana / OpenTelemetry** 22:33 I don't have any reviews, I guess, yeah.
**Michele Mancioppi (Dash0 Inc.)** 22:37 Basti, can you, can you maybe, be the one to, to help check out here?
**Bastian Krol (Dash0 Inc.)** 22:42 Yep.
**Michele Mancioppi (Dash0 Inc.)** 22:50 Is there anything else?
**Nikola Grcevski @ Grafana / OpenTelemetry** 22:54 Nope, I guess, Michele you're going to KubeCon? Anyone else?
I am.
So I'll see you there.
**Michele Mancioppi (Dash0 Inc.)** 23:03 See you there?
**Bastian Krol (Dash0 Inc.)** 23:04 I think, Antoine also just posted to the channel, so we probably should cancel also next week, right?
**Michele Mancioppi (Dash0 Inc.)** 23:11 Antoine is there, Matt Ware is there.
**Bastian Krol (Dash0 Inc.)** 23:17 I'm not.
**Michele Mancioppi (Dash0 Inc.)** 23:18 I, I would like a volunteer.
To think… so that we have been introducing Now we just merged the support for the minimum version in Java. We had that in .NET for a while.
Jack, has been, talking about, Providing a way to have the maximum version.
**Nikola Grcevski @ Grafana / OpenTelemetry** 23:47 Yeah.
**Michele Mancioppi (Dash0 Inc.)** 23:50 I think we should think it a bit through, in terms of the shape of the configurations, and maybe… Try to guesstimate, for which language is more likely than others?
Does somebody want to take on this lofty task?
**Nikola Grcevski @ Grafana / OpenTelemetry** 24:13 Yeah, you're gonna have me.
I started this.
**Michele Mancioppi (Dash0 Inc.)** 24:19 No, actually, who'd… Nikola Grcevski @ Grafana / OpenTelemetry 24:21 No, man, it was…
**Michele Mancioppi (Dash0 Inc.)** 24:22 net one.
**Nikola Grcevski @ Grafana / OpenTelemetry** 24:22 No, it was Matthew Hensley, but he's a Grafana, and I pushed him to do it.
**Michele Mancioppi (Dash0 Inc.)** 24:28 Good, then, then, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 24:31 Then,
**Michele Mancioppi (Dash0 Inc.)** 24:33 I'll send you… Nikola Grcevski @ Grafana / OpenTelemetry 24:33 I actually asked anyone on… we have people that work on .NET as maintainers, and I was like, can someone please… tell me what I need to do, and the auto-injector to not break .NET, and he took it on himself to… It's good, actually. He said, oh, I'll add the checks. I was like, okay.
**Michele Mancioppi (Dash0 Inc.)** 24:54 Thank you for outing yourself.
It's very responsible of you.
**Nikola Grcevski @ Grafana / OpenTelemetry** 24:59 Yeah.
**Michele Mancioppi (Dash0 Inc.)** 25:03 Cool.
I like the progress. I mean, we are, we are getting to a point where this stuff is getting mature. Node.js even tried to break the hell out of it.
We had a way out? Yeah, I'm, I'm pleased.
**Nikola Grcevski @ Grafana / OpenTelemetry** 25:19 Are you joining the Maintainers Summit?
Are you gonna get…
**Michele Mancioppi (Dash0 Inc.)** 25:25 When is that?
**Nikola Grcevski @ Grafana / OpenTelemetry** 25:27 Well, it's on Sunday, the day before… They are good.
**Michele Mancioppi (Dash0 Inc.)** 25:34 On the plane, unfortunately. I did, I missed the communication about it entirely.
**Nikola Grcevski @ Grafana / OpenTelemetry** 25:39 Me too, I mean, I'm just not willing to fly on a Saturday.
Because, I mean, there's one more day of a weekend.
I am with you.
**Michele Mancioppi (Dash0 Inc.)** 25:48 Think of that, and where the hell did they put it?
**Nikola Grcevski @ Grafana / OpenTelemetry** 25:52 I don't know, it's very obscure that, unless you're following detailed channels on hotel Slack, you're never gonna… somebody else told me, but I just wasn't willing to fly early. I think Tyler Jan from He participates in the OB SIG, so he told me, and asked me if I was going to be there, but I'm like, man, I don't want to fly myself.
**Michele Mancioppi (Dash0 Inc.)** 26:12 Because this was the perfect place to corner a bunch of people about injection contracts, but… Nikola Grcevski @ Grafana / OpenTelemetry 26:19 Yeah, yeah, I agree. But we have the observatories happening this year, so… We can… everybody's gonna be there, so why don't we do that?
**Michele Mancioppi (Dash0 Inc.)** 26:31 is we make it an actual topic at the Maintainer Summit.
Oh, you know what?
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:38 It was good for Europe.
**Michele Mancioppi (Dash0 Inc.)** 26:38 If he does, if he goes.
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:41 Antoine?
**Michele Mancioppi (Dash0 Inc.)** 26:42 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:43 He might be there, I thought. Yeah, he might be.
**Michele Mancioppi (Dash0 Inc.)** 26:46 Yeah, I mean, he's the perfect person to corner people.
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:49 Yeah.
Or if not, we do it in… What is it, 5 months? 6 months? In… In Europe.
**Michele Mancioppi (Dash0 Inc.)** 27:01 You imagine how excited I am to see another two seasons go by, right?
**Nikola Grcevski @ Grafana / OpenTelemetry** 27:08 Hmm, be good.
**Michele Mancioppi (Dash0 Inc.)** 27:08 I would like, I would like our project to evolve faster than a glacial retreats.
**Nikola Grcevski @ Grafana / OpenTelemetry** 27:13 BS, yeah.
That's true.
**Michele Mancioppi (Dash0 Inc.)** 27:18 I, I don't know, maybe I'm, I'm, I'm… I'm not reasonable in my expectations.
**Nikola Grcevski @ Grafana / OpenTelemetry** 27:23 You're… you're thinking too much like a startup, not like a…
**Michele Mancioppi (Dash0 Inc.)** 27:26 I'm thinking, like.
**Nikola Grcevski @ Grafana / OpenTelemetry** 27:27 Like a dinosaur.
**Michele Mancioppi (Dash0 Inc.)** 27:30 I've been far too long away from three-letter companies.
**Nikola Grcevski @ Grafana / OpenTelemetry** 27:35 Yes, yeah.
**Michele Mancioppi (Dash0 Inc.)** 27:39 All right, people.
Siou en sodesitant.
**Diego Hurtado (Dash0)** 27:44 Mikael.
**Nikola Grcevski @ Grafana / OpenTelemetry** 27:45 Yeah.
**Diego Hurtado (Dash0)** 27:45 Say for a minute.
**Michele Mancioppi (Dash0 Inc.)** 27:46 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 27:47 Okay, alright.
See you guys.
**Bastian Krol (Dash0 Inc.)** 27:49 around…
**Diego Hurtado (Dash0)** 27:49 I see.
**Nikola Grcevski @ Grafana / OpenTelemetry** 27:50 Bye.
**Michele Mancioppi (Dash0 Inc.)** 27:51 Digo, we can also huddle in Slack, then.
**Diego Hurtado (Dash0)** 27:53 Oh, yeah, yeah.
Well, since you're here… No.
