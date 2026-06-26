SIG: SIG Injector
Date: 2026-06-25
Duration: 37 minutes
============================================================

## Zoom Recording Transcript

**Diego Hurtado Pimentel** 05:10 Whoa, what's doing?
**Bastian Krol** 05:12 Hey, Diego.
**Diego Hurtado Pimentel** 05:14 I was so cool.
**Bastian Krol** 05:18 I know you.
**Diego Hurtado Pimentel** 05:19 No, wait.
Larry.
**Bastian Krol** 05:23 Oh, I'm… I'm living in Dortmund in Germany.
**Diego Hurtado Pimentel** 05:29 So, they're enjoying the weather.
**Bastian Krol** 05:32 Not sure if enjoying is the word that I would have chosen, but yeah. Where are you based?
**Diego Hurtado Pimentel** 05:40 I am in San Jose, Costa Rica, right now.
**Bastian Krol** 05:43 Oh.
**Diego Hurtado Pimentel** 05:44 So if you ever get tired of bad weather, you can come here.
It has really great weather all year long.
The rest of the stuff is not that great, but .
**Bastian Krol** 05:55 Beautiful.
**Diego Hurtado Pimentel** 05:56 Whether… whatever you like.
Over here.
**Bastian Krol** 06:00 Well, right now we have a heat wave here over in Europe, so, plenty warm here already.
**Diego Hurtado Pimentel** 06:08 Yeah, it's, temperature here is, like, I don't know, 23 Celsius?
**Bastian Krol** 06:14 Well, yeah, that sounds good.
**Diego Hurtado Pimentel** 06:16 Joe.
80% humidity or so on. You know, your skin never feels dry, So it's… What place do we? Don't recall that?
**Bastian Krol** 06:30 Nice.
Hi, Nicola.
**Diego Hurtado Pimentel** 06:36 Soon.
I have prepared… oh, sorry, I didn't have anything prepared.
I have a… An implementation of the… Python injector.
I don't know if you guys want to see it.
**Bastian Krol** 07:00 Absolutely.
**Nikola Grcevski @ Grafana / OpenTelemetry** 07:01 Yeah.
**Diego Hurtado Pimentel** 07:02 Alright, so… Share my screen.
Commissions.
**Michele Mancioppi** 07:20 Hello again.
**Diego Hurtado Pimentel** 07:23 Let me go.
**Bastian Krol** 07:24 Damn.
**Diego Hurtado Pimentel** 07:24 Can… can you see my screen?
**Michele Mancioppi** 07:28 Yes. Yeah.
**Diego Hurtado Pimentel** 07:31 Right, so I have this open telemetry injector demo that, Uses, compares the… implementation of… an exporter that uses, PyProto, and another exporter that uses our Python prototype implementation.
Until recently, it did everything except using the injector, but that was fixed. Thank you, Mikel. It now is… The injector.
the only thing missing from the OpenTelemetry injector demo, right? So, it takes a lot of time, so I'm just gonna start it, and then… What this is gonna do is, it's just gonna run two containers, and… Export some things, and then it's gonna tell us if… The result exported telemetry is the same in both cases.
Excluding things that are obviously gonna be different, like IDs and stuff like that, right? So, Okay, so it's starting, it's gonna take a while, so I'm just gonna stop sharing, and When this is ready, Where's my phone?
Good, excellent.
Stop sharing.
Okay, so if you want to discuss something in the meantime, you can.
I'll let you know when this is…
**Bastian Krol** 09:08 You're still sharing, I think.
**Diego Hurtado Pimentel** 09:11 Yeah, yeah, I finally found the stop sharing button.
Right. What do you?
**Michele Mancioppi** 09:18 We still see your screen.
And your chat with Todd.
Diego, we still see your screen.
**Bastian Krol** 09:37 And you're muted, but…
**Diego Hurtado Pimentel** 09:41 That's the second philosophy.
Well, it's right.
**Bastian Krol** 09:44 We will… we can just ignore that, and that's…
**Diego Hurtado Pimentel** 09:48 How… how do I stop sharing?
I cannot stop sharing. This is impossible. I hate this thing.
Yeah. Nice. I'll move back.
**Bastian Krol** 09:59 It's also a way to do it.
**Michele Mancioppi** 10:01 I uninstalled macOS.
That, the stuff, the stuff… Zoom.
Jack, your comment in the chat.
Yeah.
**Jack Berg** 10:19 gRPC is trivial to reimplement if you've already done the protobuf serialization bit.
It's very… it's a very thin layer on top of HTTP.
**Diego Hurtado Pimentel** 10:30 Hello, everybody, again. How?
**Bastian Krol** 10:32 Hello.
**Diego Hurtado Pimentel** 10:32 Hey, Jack.
**Bastian Krol** 10:33 Diego needs to hear that, if anyone.
**Jack Berg** 10:36 You had your chat open. I'm just gonna go on a quick tangent. So, gRPC is trivial to re-implement if you've already done the protobuf serialization bits, which, based on that context, it sounds like you had.
**Diego Hurtado Pimentel** 10:48 Yes, well, that's great news, Jack.
I don't know I know, I come… Sleep… Again, you know, I was… I was so terrified of… of this thing, you know? But, I hope I'm not sharing, and .
**Jack Berg** 11:09 San Diego, by the way, it's been a while.
**Diego Hurtado Pimentel** 11:11 Yeah, great to see you, Jack.
**Jack Berg** 11:13 That's the same.
**Diego Hurtado Pimentel** 11:14 I'm glad to see that the configuration thing got merchant working now.
**Jack Berg** 11:20 All these years later.
**Diego Hurtado Pimentel** 11:22 Yeah, right, and congratulations. Well done.
**Michele Mancioppi** 11:24 And we're gonna get some reinforcements in making sure that some experimental bits that we very much care about in the system packaging SIG get implemented in at least 3 SDKs.
**Bastian Krol** 11:48 Cool, so we don't have any actual other items planned on the agenda, so, .
**Michele Mancioppi** 12:01 I have one.
**Bastian Krol** 12:02 You have songs.
**Michele Mancioppi** 12:03 Yes. Go ahead.
**Bastian Krol** 12:05 Don't take up the whole 30 minutes, or 23.
**Michele Mancioppi** 12:11 I don't know what you're referring to.
Matt Ware is running a POC to add support for Ruby in the injector.
Ruby has a, auto-instrumentation gem.
JEM is the way the Ruby is packaged. The biggest question mark that I have for that is, the bundler. So, some Ruby frameworks want to use bundler, some don't, and right now the JAM needs to know which one it is, so it would not be ready for prime time for us.
But, I am pretty sure there is a way to work around that, because… We had it working at Instana back when, so… There must be absolutely a way to be able to interact with cookie.
Through the RubyOps environment variable, without having to know if a vendor is there or not.
And I also think I made some investigations, I think we would be able to support PHP as well.
I tried to reach out to the PHP SIG about that in the Slack channel.
And I've not heard about anything yet.
**Bastian Krol** 13:27 One quick thought on Ruby, we could… if it had, I'm not sure if it's more works or not, if it helps, it could go a similar way as with Python, by just implementing, basically, an empty support for Ruby ops without packaging any actual jam, and then people need to enable it.
On their own.
**Michele Mancioppi** 13:49 Let Matt do his magic, and yeah, sure. If we can do it out of the box or not.
**Bastian Krol** 13:55 Sure, yep, just wanted to…
**Michele Mancioppi** 13:57 That is a good fallback.
Although, for example, I don't feel we have gotten much feedback about the Python implementation that way.
**Bastian Krol** 14:06 Zero, I would say. Yeah, no, no, of course, that's a big drawback. I mean, you also don't get tons of feedback for other stuff, although a little bit here and there, yeah.
**Michele Mancioppi** 14:18 But, for example, for PHP, Nicole and Jack could go and ping Cydriced, see?
Doing fake, yeah.
They say, hey!
Because he's technically in the PHP SIG.
**Nikola Grcevski @ Grafana / OpenTelemetry** 14:31 Oh, I see. Okay, I didn't know.
**Michele Mancioppi** 14:34 PHP instant tracers back when, so I… I know he will be gay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 14:39 Oh, that's.
**Jack Berg** 14:39 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 14:40 Alright, we gotta ask Cedric to see what we can… yeah.
Somebody opened a Ruby issue, and they said they want to work on it. I don't know if you saw the…
**Michele Mancioppi** 14:52 I'm aware.
**Nikola Grcevski @ Grafana / OpenTelemetry** 14:53 issue on the injector. Somebody recently opened a Ruby injector issue, and they said they would like to work on it.
**Michele Mancioppi** 15:00 Is that Matt?
**Bastian Krol** 15:03 I mean, I think we had an inject… a Ruby issue since… Over a year, that it was opened by… By Antoine.
**Nikola Grcevski @ Grafana / OpenTelemetry** 15:14 It's Matthew Ware.
**Michele Mancioppi** 15:17 Yeah.
**Bastian Krol** 15:21 Wait a second, do we have… oh, this is… okay.
Now we have… 2 or 3 Ruby issues.
**Michele Mancioppi** 15:29 Excellent. The more, the merrier.
**Nikola Grcevski @ Grafana / OpenTelemetry** 15:32 Whatever gets you done, right?
**Michele Mancioppi** 15:34 Wait a second, I would like to point out that the oldest open issue Buy the support.
Can we call this closed for now?
**Diego Hurtado Pimentel** 15:50 Sure, it's… everything's working now, I can… I can show you.
**Michele Mancioppi** 15:55 Right, no sure way.
**Diego Hurtado Pimentel** 15:58 I can now share my screen and show you that you can officially close the e-shirt.
Oh my god, this is so scary.
**Michele Mancioppi** 16:09 The shared settings of Zoom, right?
**Diego Hurtado Pimentel** 16:12 Sort of what?
**Michele Mancioppi** 16:13 The shared settings of Zoom are scary, yes.
**Diego Hurtado Pimentel** 16:16 Yeah, I… alright, let me see if this… Kinda works.
Okay, deep breath, here goes.
Can you see my screen?
**Michele Mancioppi** 16:31 Yep.
**Diego Hurtado Pimentel** 16:32 Okay, this is very anticlimactic, I guess, but… everything is green, it works. So, there's a little script, around the pipeboard above, which is the Python proper implementation, and, started a container, and, exported some… metrics and logs and traces. Then we did the exact same thing, but using the protograph exporter and It compared things, and everything is the same.
You're gonna have to trust me on this one.
But, yeah, it works.
**Nikola Grcevski @ Grafana / OpenTelemetry** 17:10 Sounds good.
**Diego Hurtado Pimentel** 17:11 Stop sharing now.
**Michele Mancioppi** 17:12 So, how would we go about… publishing this, because ideally, this would be upstreamed in the… in the Python SDK.
**Diego Hurtado Pimentel** 17:23 And the…
**Michele Mancioppi** 17:23 I can imagine it's gonna take a bit.
**Diego Hurtado Pimentel** 17:28 Sorry, you…
**Michele Mancioppi** 17:30 Let's go with the.
**Diego Hurtado Pimentel** 17:31 stupid.
**Michele Mancioppi** 17:32 Upstreaming the new exporters in the Python SDK and releasing a first version.
**Diego Hurtado Pimentel** 17:38 Well, the Python SIG is right after this meeting, so if… I am persuading enough, I guess, that.
**Michele Mancioppi** 17:47 Excellent.
Yeah.
**Diego Hurtado Pimentel** 17:49 Oh.
**Michele Mancioppi** 17:49 Actually, I'll actually consider… Consider attending.
Yep.
**Diego Hurtado Pimentel** 17:57 Yep, so if you want, you can just, to enforce this, and…
**Michele Mancioppi** 18:02 I'll come, I'll come and support. Yes, Jack?
**Jack Berg** 18:05 Hey, I missed the beginning of this meeting, but, Diego, how… how does this work?
So, like, what I'm gathering is that you've kind of re-implemented the protobuf serialization, for HTTP protobuf, and therefore can drop that toxic dependency?
**Diego Hurtado Pimentel** 18:26 Wow, how does this work? Jack asking the hard questions is right over, right?
Yes! Yeah, you're right.
**Jack Berg** 18:35 No, I just mean, like, because I know it can work a couple of different ways. You can do it in Python itself, or you can do it, like… I think, you know, Alex Bowen was discussing, you know, a Python re-implementation that, you know, was built on top of the C++ SDK. And, you know, I guess I'm just implemented and just, like, interested in, like, how the implementation actually works. Like, is it a pure Python thing, or is it trying to do something lower level?
**Diego Hurtado Pimentel** 19:03 it is a pure Python thing that is trying to do something lower level, both things, so… Okay,
**Michele Mancioppi** 19:14 What's the code?
**Diego Hurtado Pimentel** 19:16 Yeah, you can see my screen again, right?
**Jack Berg** 19:18 Yup.
**Diego Hurtado Pimentel** 19:19 Okay, great rates.
So, what I did was I… I created this OpenTelem… so we had this OpenTelemetry protocol package, which contains the classes generated from the protocols, right? So, I created this new OpenTelemetry PiProto, and inside, here is a little extra package that's named PyProtograph.
So, and you see here, scholars, fields in them, so what I did was, I… I read the documentation on… Of… protocol of encoding, and I understood how it works, how the big Indian and the little Indian, and the bits and bytes and everything, right, works. And, I implemented it again for the basic types. So, for example, for scholars here, we have a Python implementation that does the encoding in the same way that, Answering it, Alerto.
Parent. Parent is the main type, right? So, just an example, right?
So we take the… the bytes, and we do, we take the first one, we leave only 7 bits, and then we do this end operation and stuff. So everything that Protob does, we are doing in Python, and from there, we are replicating… replicating the… the… the tags of Protobuff, then the fields, then the proto… protobuf classes that were generated automatically, and then the… we create a new supporter that uses this, so we are basically replacing it at the lowest level. So yeah, it is, an implementation that is doing bit and byte handling, but in Python.
**Jack Berg** 21:18 That's… that's very cool. We… from what it sounds like, it sounds, like, identical to what we do in OpenTelemetry Java.
And, I guess one comment slash recommendation, I think, you know, you were… you were comparing the… the output Of, like, you know, one export payload versus another, and saying, like, you know, with the exception of the things that are subject to change, like identifiers and timestamps and things like that, like, everything else is identical.
And so, yeah, that's a big challenge for us, or was a challenge that we solved in our Java implementation of this, is making sure that our hand-rolled serialization was, like, bit-perfect, to what the protobuf library serialization was doing. And so, we basically have this huge test suite that, you know, builds up the payloads.
that we want to encode, and then we'll run them through the Protobuff serializer and our hand-rolled serializer and compare the results on a bit-by-bit level. And, you know, that's how we kind of gain confidence that, like, our hand-rolled solution is working. And so, you know, for each and every type that composes the, you know, OpenTelemetry proto, we, we would, like, generate payloads and do this, you know, bit-by-bit comparison against the protobuf library, so… Yeah, that's kind of how.
**Diego Hurtado Pimentel** 22:45 Yeah.
**Jack Berg** 22:45 instill confidence in yourself and in the Python sig that this is actually working.
**Diego Hurtado Pimentel** 22:51 Yeah, we did, the exact same thing. We created these test cases that, use the actual protobuf library. So actually, Protobf is a dependency of this package, but only a test dependency.
**Jack Berg** 23:05 Exactly.
**Diego Hurtado Pimentel** 23:05 So we… we compare that, okay, we tell Protobf, okay, encode this thing, and we tell the… our encoder, encode the same thing, and we compare that the bytes are exactly the same thing. So we did the same thing.
**Jack Berg** 23:17 Very nice.
I love it. This is… this is overdue. I hope that the Python SIG is welcoming of this contribution.
**Michele Mancioppi** 23:27 If it is not. We could still… Keep it for now in, in our repository, and, ship it with images, and in the, in the system packages images.
**Nikola Grcevski @ Grafana / OpenTelemetry** 23:41 Yeah, that's what I was gonna ask, so can we do that?
Then we have our own… instead of taking the upstream… hotel, operator… Dependencies, we have our own that are… Using this.
**Michele Mancioppi** 23:53 We have our own dependencies for that, I think, right?
No, I'm thinking of… there's the operator, no. But we can copy the list from over there, and then add the.
**Nikola Grcevski @ Grafana / OpenTelemetry** 24:03 Yeah, and add this. Replace their proto buff with this one, and make sure that we have our own package that we maintain now in our repo.
**Michele Mancioppi** 24:11 Yep.
**Diego Hurtado Pimentel** 24:12 Yeah.
**Bastian Krol** 24:12 What do you mean, the Python dependencies? I mean, right now, the dash zero operator and the OpenTelemetry operator use the same list, basically. It's a copy.
**Nikola Grcevski @ Grafana / OpenTelemetry** 24:24 Say, same, same as us, yeah, same as us.
**Bastian Krol** 24:26 Yeah, yeah, yeah, exactly. Everyone uses the same, but… And in the injector, we don't have any right now. We don't provide the packages yet, but of course, yeah, we would then use this new…
**Michele Mancioppi** 24:39 We could. Exactly. I also want to do it in the system packages, so the moment I delete the packages, I can, it's 10 minutes to add, the Python, the Python packages.
**Diego Hurtado Pimentel** 24:54 Yeah, I was also wondering if this scenario where in Python, right, where we have a problem because of conflicting dependencies, is also happening, maybe not only injector, but maybe in the… just in the plain instrumentation side of.
**Michele Mancioppi** 25:10 Hey, too.
**Diego Hurtado Pimentel** 25:10 iPhone?
**Michele Mancioppi** 25:11 Yeah, yeah.
**Diego Hurtado Pimentel** 25:12 Well, huh?
**Michele Mancioppi** 25:12 It shows up in, usually it shows up when you do the, when you add with whatever package manager you want in Python, the auto SDK, then you need to go and resolve those dependencies, and then it's a pain.
**Diego Hurtado Pimentel** 25:24 Right, so then this could be a solution also for that problem, so that should make it even more convincing for the Python containers to accept this?
**Michele Mancioppi** 25:36 Python is breaking one of the unspoken rules of creating SDKs that people do not regret.
And it is not have any dependencies, that is not just libraries with a runtime.
**Diego Hurtado Pimentel** 25:48 Yeah, those Biden guys, you know?
**Jack Berg** 25:50 It's just really hard to, to… to take on the… the load of re-implementing protobuf, re-implementing gRPC, especially in, like, the pre, like, LLM era. Like, it's probably pretty fast to do that now, but, like, back in 2020, when these SIGs were kicking off and had a bunch of shit to do, like, that was a tall order.
**Michele Mancioppi** 26:13 Yeah.
And it's also not, not.
**Bastian Krol** 26:16 Correct, I mean, Node, Node also has a couple of…
**Michele Mancioppi** 26:18 Node does not… nobody dies if you have a duplicated package in NodeMarket. Right.
**Bastian Krol** 26:23 It's about that.
**Michele Mancioppi** 26:24 We have a concept of class loading, so that is.
**Bastian Krol** 26:26 Yeah.
**Michele Mancioppi** 26:27 Which way you can do that.
**Bastian Krol** 26:29 Yeah, yeah.
**Diego Hurtado Pimentel** 26:29 Yeah, no.
**Bastian Krol** 26:29 Exactly. It's less a failure of the language 6 as its differences in how loading dependencies work in different runtimes, that's my…
**Michele Mancioppi** 26:40 The less support you have to do civilized things in the language and the runtime, the harder you need to work.
**Diego Hurtado Pimentel** 26:46 Yeah, but that's also a problem that doesn't just happen to everyone.
in the same way, it's not equivalent, right? Because, no doesn't have this problem, because they have, like.
their dependencies can have their own dependencies, but Python dependency managers are sucks, so we are…
**Michele Mancioppi** 27:04 I'll… Quite frankly, of the languages that have the biggest issues with that.
Python is the first and foremost by a mile.
**Diego Hurtado Pimentel** 27:12 Nope.
**Bastian Krol** 27:13 One quick… one quick detail question about… Python, if this is now a different package name that provides the exporter, how is any of the other OpenTelemetry packages referencing the exporter by a specific package name, and does it cause any issues?
**Michele Mancioppi** 27:33 Yeah, I mean, the declarative configuration in Python probably will end up referencing directly the package.
**Jack Berg** 27:44 Hmm, doesn't need to.
Depends on how you organize stuff.
**Michele Mancioppi** 27:49 I have not seen that there is a PR for the credit configuration implementation, I have not seen what it does internally. But if there is something, it's likely that.
**Bastian Krol** 27:59 Hmm.
**Jack Berg** 28:00 Yeah, and I think what you're referencing is the fact that declarative config needs to, you know, reference and create things like OTLP exporters.
**Michele Mancioppi** 28:10 Yes.
**Jack Berg** 28:11 So in Java, the way that we organize it, so the declarative config package doesn't have dependencies on everything. The declarative config package actually has no dependencies, and the task of of taking a configuration, you know, YAML mapping, like a node, and transforming that into an OTLP exporter, or a Jaeger sampler, or this. That's a distributed task, so those little chunks of code are distributed across all the packages that actually contain those components.
So I think that that's the…
**Michele Mancioppi** 28:45 Oh, nice.
**Jack Berg** 28:46 The ideal way to organize it, decentralize it.
**Michele Mancioppi** 28:51 Yeah, I mean… Against… I don't know the details, but if there is something where the new package may conflict with the other one, it's probably that.
It's not an unsolvable problem, I would say.
Cool.
We have a user bug from somebody that actually was there at the unplugged Hotel Unplugged in Brussel. Marco.
Where, he would like even less debug output.
**Nikola Grcevski @ Grafana / OpenTelemetry** 29:28 Yeah, I saw that. It's similar to what Jack works on, yeah.
**Michele Mancioppi** 29:34 This is because the injector is not granted access to the process environment.
So if, if we do… if you cannot read the log levels in the process environment, then, What Mark is asking is that the injector goes entirely silent.
Or only logs at debug level.
**Nikola Grcevski @ Grafana / OpenTelemetry** 30:00 I mean, that's reasonable. Maybe permission-related stuff, yeah?
True.
But then… In the usual cases, we will not know that something went wrong.
That they didn't give us enough permissions?
**Michele Mancioppi** 30:14 No, but this is an explicit error where, I don't know what the heck is the Libsy implementation for… I'll end up doing here, but it's… it's throwing an error where it just has new.
I don't know how the triggers…
**Bastian Krol** 30:30 Yeah, I think that is… that is even happening before lip-C detection, right? I mean, that's where we read the lock level, which we do early, before the lip-C detection, by reading it from proc self.
NVRON, or something like that, and that's where this is failing, and then I guess it's already aborting everything else, I would guess.
**Michele Mancioppi** 30:53 This sounds like we just need to add error access denied in the same clause with error rate failed.
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:02 Hmm.
**Bastian Krol** 31:03 Yeah, might be. I don't know the code from the top of my head, but yeah.
**Michele Mancioppi** 31:08 The point is, I don't know how to reproduce it.
**Bastian Krol** 31:12 Yeah.
That's a good question.
I mean, from the information that he provides, he can probably provide a fix, and maybe he can retest it.
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:25 Maybe we can construct this test, I guess.
Create something that Access to a cell phone around.
**Michele Mancioppi** 31:39 Does anybody volunteer?
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:43 I can look at it next week, I can't this week, but next week, right, yeah.
**Michele Mancioppi** 31:49 Stone Tuts.
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:54 There you go on a K, yeah.
**Michele Mancioppi** 31:56 Alright.
I, I'm bad at this.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:00 No, no, it's all good.
**Michele Mancioppi** 32:02 By the way, the, We have a version of the system packages as per the latest and greatest specification in the packaging SIG.
deck.
Nikola, if you want to try them?
Please do, because the more, the more people try them, before I go to end users and say, hey, if you try that too, the better I sleep at night.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:29 Can I… do you have a link or something? Sorry, I didn't go to that sick call, but maybe I should…
**Michele Mancioppi** 32:34 It is in the chat.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:38 Thank you so much.
**Jack Berg** 32:39 So there's a… so there's a package, and those are just being published, or the idea would be they are published just to GitHub for now?
**Michele Mancioppi** 32:50 The, what… there are multiple packages. There is actually one for the meta package, so OpenTelemetry, one for conjecture, one for languages, and there are three, and probably, like, we do Python by the next time we speak, given what Tiger is doing.
the, At the moment, to test it, you would build the packages locally, and then point APT or YAM to your local file repository.
And the agreement is when a few people inside these six have tried it, then we can publish a version, the first release, that will publish it to GitHub pages.
**Jack Berg** 33:28 Yeah.
**Michele Mancioppi** 33:29 And then the next step is to figure out the build infrastructure and the packages, and that is going to take away longer. But when we start publishing those packages on GitHub pages, then end users could technically try it.
**Jack Berg** 33:44 I have a question for you. So, like, for me, the packages, it's nice to have them as, you know, as APT install, that type of thing, but, like, what… what I think it will get more usage, because OpenTelemetry is cloud-native, is if they're bundled up as, like, images, so that they can be used in places like the… the operator. And so… so… Do you… I just want to connect the dots, because my vision is that, like, the operator someday would take its images that it publishes and, you know, rip out the internals to instead use the packages published by the packaging SIG to install, for example, the Java instrumentation, or maybe the packaging SIG publishes those images itself.
**Michele Mancioppi** 34:29 better, because the actual wiring that you need to do is different, container images. The packages will work on a container, but with your sentence of Open Direct Cloud Native, you are discounting the infinite amount of users out there that deploy software on virtual machines on Linux.
**Jack Berg** 34:44 I know, I know there's tons of them, but I'm just saying, like, you know, if I'm trying to cater to a user base, and I'm deciding, like, Kubernetes users, or, like, bare VM users, like, the priority for me is Kubernetes.
**Michele Mancioppi** 34:57 He already has an answer with the OpenTelemetry operator for now.
That answer does not exist on virtual online exhausts.
**Jack Berg** 35:06 I guess I'm just asking is, like, is the vision for you for, to include these packages, and just basically… because all they represent is a way to organize resources, a way to, like, a directory structure.
**Michele Mancioppi** 35:18 There's more for them.
**Jack Berg** 35:20 But that's one of the things that they're setting up, is a convention on how to organize resources. Do you envision publishing them into images yourself, or the operator, say, picking them up and leveraging them in the images that they publish?
**Michele Mancioppi** 35:32 I don't quite know. The, I don't… so, for example, I compared notes with, Jacob.
Who's working on, the, OpenTime transactions supporting the operator.
The, the package and seek would be the home also to delivering those… those container images.
But, before we take on that burden, we need involvement of the language sigs.
**Jack Berg** 35:58 Yeah, I know, one thing after another. I'm just talking… I'm just trying to get a handle on…
**Michele Mancioppi** 36:02 The packaging for online access on containers, on Windows, eventually is by all packaging sake?
But we are at the point are constrained by the fact that this is more a guerrilla operation than it is a widespread open territory project with support from all the people that should.
**Jack Berg** 36:24 Yep. Okay.
Well, I'll see if, I'll talk with Nicola and see if we can find a way to test this thing. I can think of a few creative ways that we can, like, exercise it.
**Nikola Grcevski @ Grafana / OpenTelemetry** 36:37 Yeah, for sure. Especially around VMs, as it makes APT and Yum packages, it'll be really cool.
See if injector's on by default. Yeah, that'll be cool.
**Michele Mancioppi** 36:46 It is on. It works.
**Nikola Grcevski @ Grafana / OpenTelemetry** 36:50 We'll give it a shot.
Okay. This will help with some customers, yeah.
**Michele Mancioppi** 36:57 I mean, at the end of the day, if, if the language seeks to not step in, Happily to support this, then the users need to ask.
So one way or the other, we need to put a spotlight on this thing.
**Jack Berg** 37:13 That's the challenge, is convincing a bunch of people in open source to pick up and care for the thing that you care about.
**Nikola Grcevski @ Grafana / OpenTelemetry** 37:19 Yeah.
**Michele Mancioppi** 37:21 if the users do care about, and I know that there is a demographic for this out there, and it's not a small one.
Right. And just need the demand… you need to make the demand feasible.
**Jack Berg** 37:33 Alright, well, I gotta run to the JavaSig, so take care.
**Nikola Grcevski @ Grafana / OpenTelemetry** 37:36 There you go.
**Michele Mancioppi** 37:37 I'll do the Python one.
**Nikola Grcevski @ Grafana / OpenTelemetry** 37:40 Alright, bet.
**Bastian Krol** 37:41 Bye-bye.
**Nikola Grcevski @ Grafana / OpenTelemetry** 37:41 Bye.
