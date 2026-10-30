SIG: Injector SIG
Date: 2026-10-29
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Diego Hurtado (Dash0)** 00:22 Hello, Antoine.
In a while.
**Antoine Toulme (Splunk Inc.)** 00:29 Hey, what's up?
**Diego Hurtado (Dash0)** 00:31 On March.
**Antoine Toulme (Splunk Inc.)** 00:38 Okay, so…
**Diego Hurtado (Dash0)** 00:40 Yeah, so…
**Antoine Toulme (Splunk Inc.)** 00:41 What's happening?
What we got?
**Diego Hurtado (Dash0)** 00:45 We got, we got, lots of, Oh, you mean related to Injector and packaging?
**Antoine Toulme (Splunk Inc.)** 00:55 I'm just very, very, very, very dumb, but open the dock, and I look for stuff, and I see nothing.
So, I'm just gonna… Attendees… Jack's not here yet. Me highly, no.
**Diego Hurtado (Dash0)** 01:16 Oh yeah, I need to add myself.
**Antoine Toulme (Splunk Inc.)** 01:19 Yeah, agenda… There's anything else that's not being talked about, so… I don't see anything in the agenda?
**Diego Hurtado (Dash0)** 01:29 29. Alright.
**Antoine Toulme (Splunk Inc.)** 01:34 Instead of being so bureaucratic, Okay.
Okay, there's no pull request, it's, like, burning.
A couple of them I was just like… Okay, update versions of Go. Yeah, let's do it.
Why not?
I'll just merge that.
But what else?
**Nikola Grcevski** 02:20 My PR about Java, and I think Nikola worked on top of it, so appreciate some reviews there.
**Antoine Toulme (Splunk Inc.)** 02:28 Alright, so… Let's go. 442.
Let's talk about it.
You're feeling better, the feeling it's ready to go?
**Nikola Grcevski** 02:45 Yeah, I mean, I looked at Nikola exchanges, he looked at mine, but… I mean, I think they're good.
**Antoine Toulme (Splunk Inc.)** 02:51 No, because it makes it difficult to… For him to approve if he's himself…
**Nikola Grcevski** 02:59 Yeah, so you see, half of the commits are from me, half of them are from him, so, correct.
**Antoine Toulme (Splunk Inc.)** 03:03 Perfect.
**Nikola Grcevski** 03:05 I added one comment. It's just a minor thing, he's sorting the directories. That's fine. I mean, I… I didn't think he mattered, that's why I never sorted them, but it doesn't hurt, so… essentially, these JVMs, they package multiple JVMs in the same build. Maybe, like, you think one is a client.
For, like, applets and client applications, one is a server.
And some of the other vendors… some of the other vendors ship their own, like, specially optimizer version.
But all of them should report the same version, so it shouldn't really matter Which one we pick to analyze to find a version?
Yeah.
It wouldn't… it wouldn't hurt if we saw it, and it was predictable, so…
**Antoine Toulme (Splunk Inc.)** 04:05 What's the rightHelf function for?
I don't see it's used.
**Nikola Grcevski** 04:11 Where is? Which one?
**Antoine Toulme (Splunk Inc.)** 04:13 In, there's a write ELF function at the end of the PR in test UTL.
I just don't see it used. I mean, I'm just… it's very dumb, like, just Command-F on the webpage.
Maybe it's hidden, you know, somewhere.
**Nikola Grcevski** 04:28 It's a test function,
**Antoine Toulme (Splunk Inc.)** 04:31 Is test something? Does it have to write… start with test in SIG to be a test function, or… I don't know anything.
**Nikola Grcevski** 04:39 Oh, okay, maybe it got removed now. I mean, I used it to kind of write a small elf, so we can prove that it parses it.
**Antoine Toulme (Splunk Inc.)** 04:49 Or is this just, like, a script you run one time to create something as a.
**Nikola Grcevski** 04:53 It's true.
Maybe. Yeah. Yeah.
**Antoine Toulme (Splunk Inc.)** 04:56 is this function…
**Nikola Grcevski** 04:58 Okay, I'll take a look.
**Antoine Toulme (Splunk Inc.)** 05:00 be removed, or… Use this function.
won't you see it.
to be used by CLIs.
**Nikola Grcevski** 05:10 Maybe not, maybe it was… Yeah, it's duplicated. I see what happened.
Is it?
Oh, no. Okay, sorry. I'll take care of that.
That's great.
**Antoine Toulme (Splunk Inc.)** 05:22 No, it's very likely what happens here is that I didn't load all the divs, so let me check.
No, still not used anymore.
**Nikola Grcevski** 05:29 No, no, I think I used it initially, but then I changed the way I did the testing. It's my fault.
**Antoine Toulme (Splunk Inc.)** 05:35 Okay.
Well, I contributed, yay.
**Nikola Grcevski** 05:40 Cool, thanks.
**Antoine Toulme (Splunk Inc.)** 05:42 Yeah, no worries. So… After that, so… What we could do is here, so let's just do a simple review if you want.
Since you're here, let's take the time.
Yeah, everybody okay with that, Jigo? You okay with that?
Sorry, let me get back to my Zoom… Oh, and hey, Jack.
Alright, so… Let's just, go through it.
Alright, so… Yes, keep interjection processes a lot, yes.
Okay.
Where are you getting into the… Weird stuff.
**Nikola Grcevski** 06:34 Beautiful.
Yeah.
**Antoine Toulme (Splunk Inc.)** 06:37 Okay, alright, so… I'm gonna mark it viewed for myself here, so… okay.
**Nikola Grcevski** 06:45 That's just testing, and it just makes small Java apps.
Damn.
**Antoine Toulme (Splunk Inc.)** 06:50 That makes sense. I've done this type of stuff so many times now, as you get so render this age… Okay.
Okay.
So again, this is for testing.
This is also for testing, so you can't, like, I built it up and just JDK8 Josie, it's… Okay.
**Nikola Grcevski** 07:13 Yeah, so there's two… yeah, there's one test. That's a normal, yeah, that's the only one I could find, yeah.
**Antoine Toulme (Splunk Inc.)** 07:19 That's an interesting one, and VolHub is a… known place, just… it's not good.
**Nikola Grcevski** 07:25 Yeah.
**Antoine Toulme (Splunk Inc.)** 07:26 Does it appear on us?
**Nikola Grcevski** 07:28 No, I think they keep vulnerable images for testing, vulnerability images.
**Antoine Toulme (Splunk Inc.)** 07:34 Okay.
**Nikola Grcevski** 07:35 I mean, I don't know if it disappears when we do, but it's the only one I can find publicly, but maybe we can grab it and publish it somewhere?
That's an alternative.
**Antoine Toulme (Splunk Inc.)** 07:47 Well, it's also referred to by Hash.
So it's so unlikely to change, right? I think you're… it's just full of… Okay, I don't see it as a problem. Okay, no… Okay, what do you need fun utils?
Because you can't find Find? Are you using find later?
**Nikola Grcevski** 08:11 No, I forget.
I forget.
**Antoine Toulme (Splunk Inc.)** 08:14 Okay.
**Nikola Grcevski** 08:15 Okay, I have to check that, yeah.
**Antoine Toulme (Splunk Inc.)** 08:18 Need to have bind.
Okay, alright.
**Nikola Grcevski** 08:24 Let's see… Amazing.
**Antoine Toulme (Splunk Inc.)** 08:28 Okay.
Test sentiment, blah blah blah, skipping… Sure.
**Nikola Grcevski** 08:38 Yeah, on ARM… on ARM we don't have any of these, yeah.
It's not… Yeah.
**Antoine Toulme (Splunk Inc.)** 08:44 Absolutely.
So again, this is the same one.
**Nikola Grcevski** 08:50 Yeah.
**Antoine Toulme (Splunk Inc.)** 08:51 Beautiful. Okay.
Alright, so we're just loading up different tests and making sure the or true… oh, because.
**Nikola Grcevski** 08:58 Yeah, I mean, sometimes my tests would fail, so, but I was working on this, so I just added Orcher in case the Docker image is not there, and I'll fail my… Test.
**Antoine Toulme (Splunk Inc.)** 09:12 Do you know how long… how long is your CI on GitHub Actions now? Is it even… maybe it's negligible, but… This might be, something to look into later, is that… we… we can use a cache with… for Docker images, pretty transparently on… on GitHub Actions. Just… I'm gonna put a comment on there, just for myself, and then maybe this can be an issue that we can open for… as a follow-up, not part of this. Okay. Like, as follow-up, we can have… GitHub Action Docker Cache.
compute to speed up CI.
So we don't download.
images all the time. I mean, we, personally, we've been getting throttled a lot, not even just for hotel, but even for Splunk stuff.
**Nikola Grcevski** 10:05 Yeah, that's just another JVM, that's Graal, that's not a… not a hotspot build, it's just another test.
**Antoine Toulme (Splunk Inc.)** 10:13 So now we're running test cases.
Yeah. Okay, okay, okay.
Alright, gym test… Sure, same idea.
**Nikola Grcevski** 10:26 Same with the same, just, they only run for x86.
**Antoine Toulme (Splunk Inc.)** 10:33 It's pretty… That's a lot of stuff. I mean, I have zero turns, it's first and Shake off. Yes, we know that much. Okay.
Okay.
Oh, okay. Yeah.
Too bad the README wasn't the first in my PR review.
So now you have this additional configuration that you can see.
**Nikola Grcevski** 10:53 Yep.
**Antoine Toulme (Splunk Inc.)** 10:54 Minimum and maximum.
I'm a major… So you're reading this information.
**Nikola Grcevski** 11:01 Invasive tests for what's valid, what's not, yeah.
**Antoine Toulme (Splunk Inc.)** 11:05 Yep.
Yeah, okay.
And so now you're applying this… Let me spell it right. Okay, so it's just, like, a very… A zig… a zigism.
Or we're reading this.
Okay.
Okay.
Okay.
So, versions allows injections, the one where all the value is? Okay.
**Nikola Grcevski** 11:41 Yes.
**Antoine Toulme (Splunk Inc.)** 11:42 We did not set that, don't care if… Major… Meetings no possible, because we're jacking to the shell browser.
**Nikola Grcevski** 11:52 Yeah, so this is the same as ignoring it. Right now, we said we're gonna change this behavior. If you specify a version, it has to be opt-in. If you say, I want minimum 8, then if we don't find it, we should abort. But this is diff… I'm still keeping the existing… behavior here, and we'll follow up with changing both .NET and Java.
To be, you require it explicitly, and if you do require it, if we don't find a version, we stand down, because we don't want to break you.
**Antoine Toulme (Splunk Inc.)** 12:23 When you said minor minimum and maximum versions, do you check that one is less than the other? Do you care?
**Nikola Grcevski** 12:30 No, we don't care about the miner, I think it's just, where you see?
No, sorry.
**Antoine Toulme (Splunk Inc.)** 12:38 The minimum, minimum versus maximum, we passed on that in,
**Nikola Grcevski** 12:42 Oh, the maximum doesn't matter. Like, we support everything forward.
Oh, okay. Just the minimum.
**Antoine Toulme (Splunk Inc.)** 12:47 Just a minimum, okay. You're not… I don't even know if I want to talk about that, but…
**Nikola Grcevski** 12:54 Yeah.
**Antoine Toulme (Splunk Inc.)** 12:55 Okay, listen.
**Nikola Grcevski** 12:56 No, we just don't wanna… yeah, we just don't wanna detect… I mean, it's true. If people had tried the Java agent with unsupported versions.
it will likely break. But that's… temporarily, like the Java team.
the Java hotel team will fix this eventually, and add support, and… It's not…
**Antoine Toulme (Splunk Inc.)** 13:17 Build contracts when we don't need to.
**Nikola Grcevski** 13:19 Yeah, yeah, yeah.
**Antoine Toulme (Splunk Inc.)** 13:20 It's okay. So it would just… Fluster people and not help that much, because, you know.
**Nikola Grcevski** 13:26 Yeah, and I… and it usually… I mean, I think the… what I've seen so far is the JavaSIQ is pretty good at keeping up with the versions that are released, but people try pre-releases, and, like, there's pre-release for Java 27, or whatever, and… And they'll try it, then it will not work, and they complain, and… That's okay.
**Antoine Toulme (Splunk Inc.)** 13:53 Okay.
So you're… you're desperately trying to get the right file so you can read it.
**Nikola Grcevski** 14:01 Yeah. Yeah, there's… yeah, it tries all different kinds of ways. It says, is it here, is it there, and… Yes, it's…
**Antoine Toulme (Splunk Inc.)** 14:08 Okay.
**Nikola Grcevski** 14:08 Labor, yeah.
**Antoine Toulme (Splunk Inc.)** 14:11 There is file version, there's autonomous VM, so that's the hard VM stuff, yeah.
Yeah. Okay.
**Nikola Grcevski** 14:17 So if we… that one is a… is a… right now, I didn't actually attempt to find it. So right now, what it does is that if it finds alternative VM through an environment variable set, it just says, okay, let it go.
We don't know what they're doing there, but…
**Antoine Toulme (Splunk Inc.)** 14:32 Well, through your reading the… okay, and the break is here when you're done.
reading from that file, okay. Yeah. And then you return, okay, okay, launcher from AppSlide, okay.
Boucher from Maps. Okay, so you… Okay, alright, let's keep going. Detect launcher versions… Oh, this is the thing you told me about.
**Nikola Grcevski** 14:59 Yeah, because they ship multiple builds of the same JDK for different flavors. One is performance, one is baseline, one is for clients, and… They're all, like, subdirectories inside, and…
**Antoine Toulme (Splunk Inc.)** 15:12 Wow.
**Nikola Grcevski** 15:13 I mean, I just let a comment, may not be important to sort, but it wouldn't hurt if some… I mean, it's probably better in the sense that if we ever have a bug in here, it will be… Consistent to replicate it.
**Antoine Toulme (Splunk Inc.)** 15:27 No, okay.
**Nikola Grcevski** 15:28 Otherwise, like, if directory scan is different for the end user, we may find a different one. It works for us, but for them it doesn't.
**Antoine Toulme (Splunk Inc.)** 15:38 Okay.
I see. Oh, that's the orders of those directories by default? Is that what they start with?
**Nikola Grcevski** 15:47 Yeah, that's right, so they have different ones, and we have a prefer, so we don't actually… we try in the preferred order to find them.
Absolutely.
**Antoine Toulme (Splunk Inc.)** 15:56 Had enough.
That's a lot of inside baseball.
No, seriously, like, this is not… like, I did not know that.
And that invoice.
**Nikola Grcevski** 16:07 Yeah.
**Antoine Toulme (Splunk Inc.)** 16:08 I was priding myself as being a Java developer, but this seems like a… A really interesting one.
**Nikola Grcevski** 16:15 Yeah, you can see how different they even named them, like, Azul does one thing, Raul does another,
**Antoine Toulme (Splunk Inc.)** 16:21 Yum.
Yeah, they're gonna have to do that, right? Otherwise, what's the point of having Azure if it's not slightly different?
**Nikola Grcevski** 16:29 Yeah.
**Antoine Toulme (Splunk Inc.)** 16:31 Okay, okay, alright, so finally, JVVM version, here we're just reading versions, we're reading the… UF?
Read CLF load segments on disks. Is that how you read the version? Oh, you're reading the… Bytecode version, this way?
**Nikola Grcevski** 16:45 Yeah, we're just reading the binary. We're reading the binary from the ELF, and then we look for the markers.
**Antoine Toulme (Splunk Inc.)** 16:51 Is it the Grafa? Has this in its,
**Nikola Grcevski** 16:54 Yeah, not the jar file? No, no. Not the jar file, the SO. The actual… the actual, actual… I will have… A symbol inside that will tell us what it is.
**Antoine Toulme (Splunk Inc.)** 17:03 Oh, okay, so you have to go all the way…
**Nikola Grcevski** 17:06 Yeah, scan for… through the SO.
And so we do one quick check that Michaela added. So Michaela added this check to say, all versions of JDK above 8. Ship this file.
And if it's there, we just read that.
Otherwise, we try to dig through this SL thing.
**Antoine Toulme (Splunk Inc.)** 17:27 What's the… what's the performance cost of doing all these checks? Because reading all this so far is not fun.
**Nikola Grcevski** 17:32 I mean, it's not fun. It's… I mean, I… I haven't timed it, but it would… it would be some overhead, for sure, not reading the.
**Antoine Toulme (Splunk Inc.)** 17:41 You're right.
Nothing's free.
**Nikola Grcevski** 17:43 Nothing's free, but the LibJVMSO is actually small.
smallish. They have… different… binaries, they're split. It's not one big giant.
Binary?
I can tell you how big it is on my disc.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 18:01 Well, one thing I was, I was thinking about, because I've been sort of following along and reviewing in the background, is, What's the criteria for evaluating this logic? Like, it doesn't much matter if it takes a little bit of overhead to detect that the Java version is compatible if we're only running it when we've detected that it's a Java process. But it matters a lot more if we're running this, like, for every process.
**Nikola Grcevski** 18:27 Yeah, so… so we don't run it for every process, right? So we first do this bunch of checks to verify that this looks like a JVM, like we look at the directories, we have to find a binary, and we say, okay, that… that is a JVM, we're gonna inspect it, and it's only then that we launch into this.
So…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 18:42 Yeah, because at one point, so that makes sense, and so, like, I think we can be much more permissive about overhead.
you know, when we are talking about, like, it's constrained to a particular branch, like, we've already evaluated that it's Java, because, like, this is all about safety, right? And the Injector, you know, its whole reputation is predicated on being able to safely inject, and so, like, you know, I would… It's hard for me to think about an overhead that would be unacceptable to… that, like, is in the name of safety. So, yeah.
**Nikola Grcevski** 19:19 Yeah, so here's what's on my disk right now.
So that's what it says.
So, it's, what, 17 megs?
Yeah.
So, we'll have to scan that.
I mean, if it's unfortunate that it cannot find the string… the string is pretty quickly into the L file, so, And we don't scan all the segments of the L file.
But, but it would, yeah.
The worst case scenario, it would have to kind of, like, read through this file.
How much is if I do… Time… 13…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 20:26 Am I correct in understanding that there's no default Java major version?
**Nikola Grcevski** 20:33 No.
No, there's not a default to our major version. We… we… like, right now, we… we try to find the Java version. If we… Don't find it.
We just let it go.
we instrument. That's a… and we talked about this behavior, but we'll change it after. So, we look for anything below, like, implicitly there. If it's below 8, we reject it right now.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 21:00 Right.
**Nikola Grcevski** 21:01 And I think 8 is set at the moment as the default, just like… for Node… for… sorry, for .NET.
But… when we… We're going to change the behavior after. We say, well, we'll ship with 0, and you have to specifically say in your config. And when you say in your config you want 8, Then, if we don't find the version, we stand down, assuming that will cause you grief.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 21:35 So, I think we should consider adding a default max major version if we're going through all this hassle to be able to detect the major version of Java. The Java agent does have compatibility problems with With, you know, bleeding-edge Java versions, and we can… we can migrate the max major version in, like, a backwards compatible way, because you can always, like, expand the set of criteria, but you, like, and that's compatible, but you can't constrain it, so we can just have that be, like, a floating version that reflects whatever the Java agent can support.
**Nikola Grcevski** 22:10 Okay, so you think we should have a maximum as well?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 22:13 I think so, yeah.
**Nikola Grcevski** 22:14 Okay.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 22:15 I'm gonna add it.
**Nikola Grcevski** 22:17 Yeah, add a comment, please. Let's… let's add it.
Because I… you're absolutely right, but that… That should be in the config, so if you just specify a maximum version, we should stand down on maximum… yeah, I like that.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 22:33 100%, yeah.
**Nikola Grcevski** 22:38 Yeah, so I just ran an experiment how long it would take for Cat to kind of walk that file. I mean, it's… whatever.
5 micron.
Seconds.
**Antoine Toulme (Splunk Inc.)** 22:51 Yeah, that's fine, I guess. We, People complain about installation costs all the time.
**Nikola Grcevski** 22:58 Yeah.
**Antoine Toulme (Splunk Inc.)** 22:58 Any overhead of anything that we add?
So, we can have a canned response, like, we don't think. The overhead is not nil, because it can't be nil, but it's insignificant in the grand scheme of things, right?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 23:11 Well, and here's the thing, so if the overhead does become an issue, basically what somebody is saying is, like, I don't want the safety check.
And so, like, we could add a config option later to be like, hey, bypass the safety check altogether, and…
**Nikola Grcevski** 23:26 0. Minimum version zero, yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 23:28 Right, and maybe we have a special value, like a sentinel value, zero, where if you set that, then we just escape hatch all this and bypass the safety check.
**Antoine Toulme (Splunk Inc.)** 23:36 If we could also do another thing, which is we could recommend that they upgrade their Java version, so they would get a more performant system in the first place.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 23:46 Well, that doesn't change the fact that the injector adds this overhead on each and every process start.
**Antoine Toulme (Splunk Inc.)** 23:52 Well, it would, from what I'm understanding, right? Because you don't read the ELF header if you can get it from the file, so it's actually cheaper.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 24:01 Oh, I see. Okay, so older Java versions are more expensive and have more overhead. I see.
**Nikola Grcevski** 24:06 All the new ones, I think, will not even touch the ELF file. Miguel added this check that there's this one file that exists on every new Java version, and he just goes and looks in there for the version, and if he finds that file, I think it's called Java version, whatever, I have to find it, if it's there, we just use it. If it's not, then we read the ELF.
And… It's much faster.
But I can measure if you want the actual overhead.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 24:33 So, where's the code that actually, like, determines that we're dealing with a Java process. Because at one point, we were talking as, like, a SIG, we're like, hey, we're not going to make assumptions that we can understand what the, like, the language is of these processes, and it seems like we're going in a different direction, and so Java's a case, PHP was another case, and I think there's going to be more of these, so I think, like, you know, we're all sort of circling the wagons around this idea that we We have to know the language that we're dealing with, and we have to have the injector be responsible with doing some of these prerequisite checks, like the one that you've added.
But, like, where does that code live?
**Nikola Grcevski** 25:12 Yeah, if you look in the pull request, just search for libjli.so, because I couldn't find a single JVM out there that did not use that binary. So, what we do is we look at the process maps.
To see what he has loaded as shared libraries, and if he founds JLI.S, that says Java, I'm gonna actually try to figure out If… if I should actually investigate a version. And if it doesn't find libjli into the process, it just doesn't do anything.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 25:50 So is the code sort of getting organized around this idea of, like, okay, there's a process, and we need to evaluate the language of the process, and that might come back as something we know or something we don't, and then based on the language, then we, like, go into additional verification, you know, branches for each of those? Is that kind of how it's shaping up?
**Nikola Grcevski** 26:10 Yes, that's where we want to go, and especially now that we're going to find that this is Java, we identify that it's safe to inject. We don't have to inject Python, the PHP, and the .NET environment variables, which customers may find Offensive, or whatever, yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 26:24 I mean, if we could do that across the board, like, you know, you know, that'd be nice, but I guess one thing at a time for us to touch on.
**Nikola Grcevski** 26:31 I mean, definitely for .NET and Java, we could take that approach. There's no reason why we're injecting everything in these processes now that we know it's Java. It's not in this PR. That was a suggestion from the SIG, but… I would probably approach that as a follow-up.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 26:51 Well, there's a lot of stuff in here I can't say I fully understand, and… And I don't think I will without, like, an LLM to guide me.
**Nikola Grcevski** 27:00 Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 27:01 But, I know you have a ton of experience with JVMs, and so, like, I think that at, like, a high level, it makes sense, and I'm, like, deferential to you on the details.
So, I guess I'll continue to, probe it with an LLM locally to see if there's, like, anything that, you know, stands out. But, yeah, this looks good to me conceptually.
**Nikola Grcevski** 27:25 Thanks. Yeah. I'll address your, the feedback. Yeah, I initially tried to do different kinds of testing, because I was gonna write that custom ELF, test against that, but then I was like, well, that's not really that good. I mean, I want to maybe find the actual binary of the JVM, see if I can find it, and make it in a test.
And then, nice.
Yeah.
Yeah, initially I was building out files and dropping them in there and having the test read them, but nothing… nothing is… as good as testing the actual problem JVM.
Yeah.
**Antoine Toulme (Splunk Inc.)** 28:08 Yeah, so…
**Nikola Grcevski** 28:08 I mean.
**Antoine Toulme (Splunk Inc.)** 28:09 I just got two comments, they're mostly small, please address them, I'm happy to approve as soon as you… as you go through that.
And, you know, the feedback from Jack, and then we can get that in, and we should make a release.
**Nikola Grcevski** 28:23 Great.
**Antoine Toulme (Splunk Inc.)** 28:24 Just in time for Capcom.
Awesome.
Awesome. Alright, I gotta run. Take care.
**Nikola Grcevski** 28:32 All right, good. Good to see you guys.
