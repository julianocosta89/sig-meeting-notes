SIG: SIG Injector
Date: 2026-05-07
Duration: 36 minutes
Zoom Recording URL: https://zoom.us/rec/share/cVHzmP3jAYlPvDCQNJolKMetlFeLP1g9QjvQa8Ccmr95iXdUTHz8mnL9ydnewSsJ.PWE_eVJF1EVjBpE-
============================================================

## Zoom Recording Transcript

**jea** 03:00 Hey, everyone.
**Jack Berg** 03:04 Hello.
**Bastian Krol** 03:07 Low.
**Nikola Grcevski @ Grafana / OpenTelemetry** 03:12 Yay.
**jea** 03:21 I can't say, too long, just heads up. But… Would love to hear what's going on, how I can help.
Everything going on there.
**Nikola Grcevski @ Grafana / OpenTelemetry** 03:37 Sounds great.
**Bastian Krol** 03:44 Sounds good.
Should we get started, then?
**Nikola Grcevski @ Grafana / OpenTelemetry** 03:52 Yep.
**Bastian Krol** 03:54 Excellent.
**Jack Berg** 03:56 Nicola, your volume's pretty low. I'm not sure if there's anything going on with that.
**Nikola Grcevski @ Grafana / OpenTelemetry** 04:02 Thanks for… thanks for telling me. I don't understand what… My… You can still not hear me, or…
**Jack Berg** 04:10 And it's better now, I don't know what you did.
**Nikola Grcevski @ Grafana / OpenTelemetry** 04:12 Better now? Okay.
**Jack Berg** 04:18 So we only have one topic, So if you have any more, please add them to the agenda, but, Bastion?
When I talk about base image versions used in tests.
**Bastian Krol** 04:29 Yes, let me open the… Agenda as well… right, so there was the… Question about the release, but we did the release, Nikola, so I guess I think it's.
**Nikola Grcevski @ Grafana / OpenTelemetry** 04:42 That's why I crossed it over, yeah.
**Bastian Krol** 04:45 discovered, exactly, yeah, right, it's, it's basic, I opened, basically, an issue about it, let me share my screen… Okay, right, what's this here? Can you see my screen? Did Zoom actually share? Yeah. Okay, excellent. So… we… we… it's a minor thing, maybe, but I think maybe it can lead into a more general discussion. So we have this PR open.
since… I don't know, a couple of months, I think. It got closed by Renovate, and then reopened, whatever. And it updates a couple of base images, and I think back then, we just said, no, let's not update at all, because these older versions, which we are on, like BookWorb, are still… Supported, or what… or something like that.
And I think maybe we should… take a second to come up with some kind of guideline, how we want to handle that. I don't think we want a giant test matrix, where we test… so this is in the packaging tests, But it could also extend to other base images that we use. I don't think we want the giant test metrics with every distribution, and every version of every distribution, and all of that. That is maybe a bit too much, so we maybe can focus on one, on my Just the suggestion is basically, Thought I opened an issue as well for that. Yeah, here.
that we maybe go with the latest supported, so always the most recent one, so not with something that is still in support, but where a newer version exists. So that would mean that, for example, for Debian, we go to Trixie enough, because that is the current stable, and Bookworm is old stable, or something like that. So that's basically… It's.
Michaela?
You're raising your hand.
**Michele Mancioppi** 07:16 Yeah, I have a point of concern on this one, and The biggest fan with Injector are old glibsy versions.
Guess what you're no longer going to test if you do what you just proposed?
**Bastian Krol** 07:35 Right, I mean, it could also break with a new version at some point, so something releases a new current stable, let's say, and that breaks it, that's… I think, I think we, we also, we have, I think two different sets of tests, and… maybe we can do a test metrics, in one of them. So we have the packaging test.
Which are really just smoke tests. They start the collector, and they start the process, a JVM with the injector, and check for a certain lock line. So these are relatively basic anyway. And then we have the injector integration tests.
Let me see… do they… no, they also only use… one specific… Base image each.
So maybe… I think the level of granularity that you talk here, like with old libc versions, which is absolutely valid, are probably a better fit for the injector integration test instead of for the packaging test. And I guess at some point, these packaging tests… Will… be moved out of this repository anyway.
Right?
**Michele Mancioppi** 09:04 Yeah, I'm, effectively, what is missing from starting the packaging SIG is the, Agreeing on, when do we meet?
**Bastian Krol** 09:15 Yeah, okay.
Okay, so you're also raising your hand, so maybe you want to chime in there?
**jea** 09:24 Yeah, I actually got bit by a similar, like, Dockerfile upgrade recently, where…
**Bastian Krol** 09:29 Hmm?
**jea** 09:29 They changed the default pinned ZIG version to 16, On, like, the stable, and it completely broke my build.
**Bastian Krol** 09:38 Yeah.
**jea** 09:39 So, we just have to be sure… I don't know how we're installing Zig today.
But that's something that, like.
Just, broke my build, and would be… Yeah.
**Bastian Krol** 09:51 That's a very good point. I think we also were bitten by that in the past. I think we are installing Zik… directly, specifically the version that we have declared somewhere, repo-wide, basically, and I think we Install that version everywhere.
**jea** 10:12 Yeah, that's what I thought I was doing, and I realized I was doing an APK,
**Bastian Krol** 10:16 Yeah, yeah, yeah.
**jea** 10:17 Install, and it destroyed my build, which sucked.
**Bastian Krol** 10:20 No, we started with… we also started with that, and that… To adopt.
**Michele Mancioppi** 10:24 Very quickly, good things.
**Bastian Krol** 10:26 So, convergent evolution here.
**jea** 10:29 Yeah, also, I do have to go soon, unfortunately, I have another meeting to get to, but I'm gonna be working on… I'm gonna bring this up in the operator meeting, but, I'm gonna start on the… like, hotel operator injector integration soon, and Michele, I'd love to maybe chat with you sometime in the next coming weeks about any lessons learned from the dash zero operator.
And, I mean, it looks at your code a bunch, but would be good to hear any, any, Improvements that you think.
**Michele Mancioppi** 11:02 I, I understand from, so at KubeCon, there was, A graphanista that wanted to volunteer for that.
**jea** 11:11 Yeah, that's Arthur. I'm gonna chat with him and pair with him on this. Cool. Yeah, but there's some… there's some, like, pre, refactoring work that I signed myself up for, that I gotta do, so… That's… but I'm going to begin on it soon.
**Bastian Krol** 11:28 Awesome.
**Michele Mancioppi** 11:29 Do you have, my Calendly?
**jea** 11:32 I don't think I do. If you want to send that to me, that'd be great.
We'll probably reach out, like, next week, realistically.
**Michele Mancioppi** 11:41 Sounds good.
**jea** 11:43 Cool. Okay, I gotta go, but, good stuff. If you need any reviews, Bastion, on any of this, just let me know.
Cool.
**Michele Mancioppi** 11:52 By the way, send me your… I don't find you in the CNCF Slack.
**jea** 11:56 I'll… I don't know how that's the case.
**Michele Mancioppi** 11:58 Tap it in the chat.
**jea** 12:01 I just, messaged you. Okay. Thanks, everyone. See you later. Have a good day. Bye.
**Bastian Krol** 12:07 Bye.
Yeah, I mean, we also don't need to come up with, going back to that base version stuff, we don't need to come up with something right now. I think there are forces pulling in either direction. I remember we also opened the Desk0 operator repository, we have a test structure that test across different base images, so that's also nice.
But I don't think that should go into the packaging test specifically. That should probably be at some other layout that is a little bit faster also.
**Michele Mancioppi** 12:47 Assume that the packaging test, moves on from this repository in the foreseeable future.
**Bastian Krol** 12:53 Yeah, exactly. So we can also shelf that for now, if the packaging stuff goes away from this report in, like, a Two or three weeks, we don't need to do something around that.
But still, I mean, the general question is against which versions of whatever, there are a couple of things where we have versions, and against which versions do we test, and which versions do we officially support. That's still a… I mean, that's a very broad question, but it's a question that we probably need to have some policy on at some point.
**Michele Mancioppi** 13:33 I am going to say something that will make you… Probably unhappy.
**Bastian Krol** 13:40 Yes, you do.
**Michele Mancioppi** 13:41 Yeah, that's… that's my privilege.
We don't get to just make a supported or not supported.
Not supported must be the absolute exception.
Because when people use the injectors, they're not gonna know what the hell we're going to try to inject.
**Bastian Krol** 14:02 Yeah, no, that's fair, and I think I agree… It's still the question, I mean, the question we… or the statement we try to support basically everything that has been around in the last 20 years, or whatever is fine.
**Michele Mancioppi** 14:20 Absolutely.
**Bastian Krol** 14:20 We still need to come up with what do we test against explicitly, and that needs to be more than just gut feeling.
**Michele Mancioppi** 14:28 Realistically, if it is any consolation, LD preload became viable 15 years ago, not 20.
Nicole?
**Nikola Grcevski @ Grafana / OpenTelemetry** 14:45 Yeah, I thought that maybe, for this packaging test, we can just upgrade to the latest image, because it's just we're testing one image, so which one? As good as any others, I don't think we should block on that.
But I think your point is valid. We probably should come up with some sort of, like, test with… with some… At least what we claim to support forward.
I mean, the easiest one to be, probably, is to look back, and of the major Linux vendors, which distro or versions are still supported, or will be supported?
maybe do a spot test. Oldest, Red Hat.
whatever is… I think Redhead goes furthest back.
And then test with couple, rather than each individual one.
**Michele Mancioppi** 15:35 Before joining, so, between Instana and, the next observability company.
I had a stint in Canonical Product Manager for Ubuntu.
It is a running joke. I mean, canonical PMs.
that, each Ubuntu version is supported forever.
And you see it, every time there is a major release, they extend the support period of ESM.
That's because people just don't move forward.
The, what is officially supported, if you go to the support that people will pay for, is effectively everything under the sun.
So it doesn't help?
And if it is only the ones that people get support for free, Not very useful.
containers… Maybe it gets better, but I bet… that there is container images out there that are based on Ubuntu stuff.
That was out the first day Docker was born.
So I don't know if that really helps as much.
Unfortunately.
**Bastian Krol** 16:39 Heck.
**Nikola Grcevski @ Grafana / OpenTelemetry** 16:40 But if you go end of life, like this website.
For example, there's… or the various… I'm just gonna paste it here.
If you look at that one in particular, it shows you when the support ended. So if you do have…
**Michele Mancioppi** 16:59 It is incorrect.
It is not, it is not when the support ended, because you can pay for, STLs.
You can pay the canonical, and you can support for the, like, 15 years ago.
It's, this is what you get out of the box without a commercial contract.
**Jack Berg** 17:18 Well, until the customers start paying the injector maintainers, I think that we can be a little bit.
**Michele Mancioppi** 17:26 Yeah, I don't know how I feel about that. I feel the responsibility of not breaking people.
**Nikola Grcevski @ Grafana / OpenTelemetry** 17:31 I mean, if you look at… I mean… I agree that if you pay extra, you will get more, but… I think eventually security patches stop coming up.
Like, if you look at the two lines, yeah, maintenance and security support, then if you look at the extended hardware and maintenance support.
That goes through 2022 onward.
**Michele Mancioppi** 17:53 No, it's much more complicated. That website is incorrect. You can get the… for example, there is the support, and I'm talking just canonical, I'm not nearly as familiar with Radhat. You can get patches for main, if you pay the commercial support for, like.
I don't remember the number, but it's, I think, 18 or something, so… bloody old, right?
**Bastian Krol** 18:18 But I think, what Jack said, right? I mean, we have to start somewhere. Right now, we test exactly one version, and I think it's an iterative process. We should maybe start testing against, like.
current stable and not end of life yet, and then we can extend from there at some point, but it's… I mean, it's… it's, diminishing returns, right? There are people who use images from the Stone Age, but it's… Not that many, so we should focus on the… On the… not end-of-life images first, and then if something comes up, we can extend.
**Michele Mancioppi** 18:59 You will never hear me complain about adding tasks for more distros. Dropping tasks for older distros, that is where my eyebrows go up.
**Bastian Krol** 19:08 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 19:09 Yeah.
How late?
The other thing is, like, if you are on the major cloud vendors and using this in Kubernetes, they'll move you up. They're not going to support you.
So, they'll push you up, force you to upgrade. Even if you pay them extra money, Yeah.
**Michele Mancioppi** 19:28 No, not in containers, Nicola. And, for example, for the OpenTelemetry operator, it doesn't have any such restriction.
**Nikola Grcevski @ Grafana / OpenTelemetry** 19:38 No, I know the operators and a restriction, but I'm telling you that in terms of, like, the base, I guess, the containers, a customer can use an old… Container image on top of… Whatever, but then, if you're using something old, then you're likely not up to date with security patches and whatnot.
So, if you look at Red Hat, they still technically support 5. Versa 5.
which is quite old. It's 2008. So, Enterprise… Redhead Enterprise Linux, I mean, actually, no, I'm reading this wrong. Right now, the only ones that are fully supported are 8.
9 and 10, according to this.
I don't know, I've never worked for any of these vendors to know that.
**Michele Mancioppi** 20:29 You go Ubuntu Pro, you go way back.
I think I'll… Jack has the hand raised since, like, 5 years.
**Jack Berg** 20:39 I just want to, kind of take a step back and think about, like, what… What are the… what are the things that could cause us to break?
You know, rather than just talking about, like, the operating system, like, what are the characteristics of, like, you know, a really old version or a really new version that could cause the injector to stop working? And I could think of three, dimensions. And these dimensions are things that you might, include in dimensions, in, like, a matrix, test.
And, you know, there's the operating system, which is what we're talking about, so the operating system distribution and the version of that distribution.
there's the, the language that we're trying to inject in, so, like, Java.NET, whatever, and then there's the, like, what… how the process that we're trying to inject in, like, how it, how it links libc. So that this is, like, one of the things that we ran into recently with, like, this old Red Hat Enterprise Linux situation, where it was, you know, there was a process that was… you know, bound in a way that we were, we didn't support, right? So, like, I don't… I don't care about adding test cases that only run in CI. I don't want them running on my machine when I run a build, but if they run on CI only, I don't care about having, like, a huge test matrix. But I do care about, like, if that… like, if that matrix is really, cluttered in the repository. Like, it needs to be… it needs to be, like, clean and tight. Like, what are the dimensions that we want to test along?
And what are the parameters for each of those dimensions?
And if we can parameterize this test.
And, you know, make it simple, and when we run locally on our machines, we just run with, like, you know, the latest of these, and when we run a build on CI, we run with all of the, you know, dimensions of the matrix, that's fine. I think that kind of is the best of both worlds. Like, fast tests locally.
uncluttered repository, but the ability to have a really big matrix up on CI.
So, yeah.
**Michele Mancioppi** 22:54 The first point you said, the distro, that's actually a proxy for a combination of libc and Linker.
Unless we're talking about those absolute maniacs of Gen 2 and Arch, which actually have different user lines for muscle and deep C, I think. In reality, when you take, like, any Debian Ubuntu, Rattat.
The lipc and the linker is just… it's one for the entire distro… distro train, right? So, when you're setting the end, the linker, it is the lip-sy, the linker, and the runtime.
**Jack Berg** 23:34 Right.
And so, like, I don't… like I said, I don't have a process… I don't have a problem with, like, having a big matrix, as long as, like, the dimensions and their values are well-defined. And then, I think what would be interesting, though, is, like.
If, like, let's say we have a matrix that starts to develop, and we have, like, you know, 5 distributions, and 5 versions of each of those distributions, and then, you know, 4 different programming languages, and, you know, two different classes of… there are 5 different classes of how the binaries are sort of, like, compiled, and how they link.
That's a lot of cases, but whatever. Let's say somebody adds a new one, and, like.
we have to… it, like, breaks. It, like, doesn't work.
Like, and we have to actually start modifying the code to accommodate this new this new case in our matrix. Like, that's when the conversation gets interesting, is when you can, like, have a case in the matrix that, like, that does not pass what we're doing today, because that's when we actually have to do something outside of the normal, like, you know, code flow to support them. So, you know, I think we can react to that. Like, if we come across that case, we can, like, make a decision and start to, like.
you know, come up with some guidance on, like, when and why we say no to certain things. But, like, you know, I can't imagine what that case looks like right now.
**Michele Mancioppi** 24:55 No, I mean, I went to incredible pains last year to figure out a way that would work in every single lip seed that I know of, so…
**Jack Berg** 25:03 Yeah, so you…
**Michele Mancioppi** 25:04 No, right? Bye.
**Jack Berg** 25:06 You already did a bunch of that work.
**Michele Mancioppi** 25:07 weird. There's always something weird, like, you found Ryle from the Stone Age that didn't link the right way.
**Jack Berg** 25:13 Right, and that was a case where, like, you know, let's say that would be an example of, like, adding a new case to the matrix.
And we didn't care about that. We're like, great, yeah, this makes sense. Let's extend the matrix to support this, because we want it. But, like, what would it look like to have to… to find a case that doesn't work, and to have, like, the code that accommodates it be, like, super ugly, or be, like, a big performance regression for, like, all the other cases in the matrix?
I can't imagine what that would look like, but that's… that's the type of thing that would have to happen for us to, like, reject supporting something.
Maybe it will happen, maybe it'll never happen.
**Michele Mancioppi** 25:50 I am sure at some point we'll find some absolute maniac that found a way to do something to dynamic symbols that we never imagined, but… I don't know. It's, like, in my ideal world, whenever there is a new major release, like a new version of Ubuntu, a new version of RAL, we take one of those images and automatically add it to the matrix in CI, and we just do it.
**Jack Berg** 26:12 Yeah, and we might have to be a little nuanced about it, because… did you say major versions? Because we obviously don't want, like, every single increment little version, right?
**Michele Mancioppi** 26:20 Never in my life have I heard of major changes in libc and Linker in the scope of a version, because very often, if you do something like that, you end up rebuilding the entirety of main and universe in Ubuntu and Debian terms, which is end of the world for package updates, so…
**Jack Berg** 26:41 Yeah.
**Michele Mancioppi** 26:42 It's unlikely.
**Jack Berg** 26:43 So just to give, like, a little color about how we handle this in OTel Java. So, OTEL Java, like, Java has releases, and Java has minor releases and major releases. And so, like, every fourth release number is a major release. So 17 is major, and then 18, 19, 20 are minor, then 21 is major, and I think you all know this already. But, like, so what we do is we, in our test matrix, we… Test every major version, and the latest minor version.
So we, like, pin to the latest minor, and then, like, other than that, going back in history, it's only the majors. So we could do something like that, you know, for the distribution versions that we decide to test in our matrix.
**Michele Mancioppi** 27:24 That would work. We end up adding one version of Ubuntu every two years, one version of Debian every… every time the Pope dies.
And then one rail every how often?
It's also 2 years, right?
**Bastian Krol** 27:38 What's… what does it… does anyone know from the top of their head, roughly, what the collector does?
What would they…
**Jack Berg** 27:45 test against for their matrix, like versions of, like the OS, versions of…
**Michele Mancioppi** 27:52 Yeah, but in the collectible.
The collateral literally doesn't give a hoot about the base image in a container image.
The way that currently it interacts doesn't.
**Bastian Krol** 28:01 Yeah.
That's right, I mean, it's just a… just a go binary in the end. And also, it probably needs to support a… less.
large set, because you can just… if you run it in the container, you'll probably give it a base image that works, and that's that, and… we need to run against… more.
**Michele Mancioppi** 28:26 Now, purely technically, the collector should ensure that Like, the same thing, like, any container-based image should still work. The moment the collector moves to the injector, then they should also do that. But the way that the collector injects today, by just setting environment variables specific to the runtime.
Then, you do not care about the lip-sy. You literally just care about the runtime. So, if they… if I had to maintain that, I would say, okay, I'm going to… to test every single JVM, I'm going to test every major release of Node, I'm going to… I don't know what I'm going to do for Python, because I think it needs an exorcism, so maybe test harder there.
But for civilized runtimes, that's the major ones. We have a bigger problem, because it's not only the measure for the runtime, it's also the combination of Linker and Libsy as they come out with the pictures, right?
**Bastian Krol** 29:19 Yeah.
Yeah, I've tried to put some of Zaps into the agenda document, because we are also so bad at keeping notes, I try to keep some. You can have a look if you agree with the stuff I wrote there, or I extended, or… edited.
**Jack Berg** 29:42 Yes, sir.
**Bastian Krol** 29:42 Yeah, I guess it…
**Jack Berg** 29:43 Let's just come up with, like, an issue to… to track this. We don't have to do this today, we don't have to block, you know…
**Bastian Krol** 29:50 That's already there.
**Jack Berg** 29:51 Okay, there's already an issue, great.
**Bastian Krol** 29:53 Yeah, yeah, I'll link it in the agenda document, so… I think the issue maybe talks mainly about the packaging test, but we can extend the scope because we probably want to discuss it in a broader scope.
And the packaging tests are not so super relevant for that.
**Michele Mancioppi** 30:23 Is there a civilized automation to discover new tags of the Ubuntu image.
For new versions?
**Bastian Krol** 30:32 We already have said, it's renovate. It tells you when the collector base image can be updated, and then it opens the PR.
**Michele Mancioppi** 30:41 Not sure…
**Bastian Krol** 30:43 test metrics once we go to test metrics, but I think that that's a solvable problem.
**Michele Mancioppi** 30:53 If Renovate can do that, great.
I've never seen it used in an additive fashion, but…
**Jack Berg** 31:01 Paycheck.
**Bastian Krol** 31:03 Me neither, but I'm sure there's something for that somewhere.
**Jack Berg** 31:06 Yeah, we… okay, yeah, this is… We… Renovate can update a matrix.
B.
**Bastian Krol** 31:17 I know it is quite powerful, just that nobody knows how to configure it correctly, is my impression.
**Jack Berg** 31:26 Here's an example of our test matrix in OTEL Java.
And, there's a comment in there, which I think it gives an instruction to renovate to update this version of the matrix to the latest Java version.
**Bastian Krol** 31:44 It probably will change the… the PR will probably change that version, but then you just…
**Michele Mancioppi** 31:50 But aren't it equal?
**Bastian Krol** 31:52 Good, yes.
Huh?
**Michele Mancioppi** 31:55 Aren't you missing 24?
**Jack Berg** 31:59 24 is not stable. It's not a fourth version.
**Michele Mancioppi** 32:06 Yes, you're right. Yes.
**Jack Berg** 32:10 Yeah, so, like, I don't think it's smart enough, or at least I don't think we've configured it to do something like add the major versions and bump the minor versions, that thing that I was talking about.
But you know, that doesn't happen as often, and so maybe, you know, once in a while, we manually intervene, but it can at least keep the tip up to date.
Within a matrix, which is something.
**Bastian Krol** 32:34 Good.
**Michele Mancioppi** 32:41 And, what does OBI test against?
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:45 We primarily are concerned with our kernel versions.
Yes. So, we picked a kernel version, Nice.
**Michele Mancioppi** 32:53 at 13.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:55 I think it's lower than that, 5'10, I think? 5'8", 5'8".
5.8 is the lowest one we support.
Because technically…
**Michele Mancioppi** 33:03 PDF was usable for what you're doing since 418, if I recall correctly.
**Nikola Grcevski @ Grafana / OpenTelemetry** 33:08 Yes, 14 does work, but only on Red Hat, because they backport the backport.
**Michele Mancioppi** 33:15 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 33:16 So, ref had… Backboarded all the good stuff.
It's… yeah, it's primarily around, which version the… they have this BTF database that describes how the offsets shift in the kernel from version to version, and that's the major, sort of… and 5.8 became the default.
And also, I think Rain Buffer was introduced and stuff like that, so we didn't want to support anything older than that. We had to pick one and pick our battles.
**Michele Mancioppi** 33:49 At Infana, we actually found a way to discover the offsets at runtime.
And I'm pretty sure we committed it to a repository.
**Nikola Grcevski @ Grafana / OpenTelemetry** 34:00 Oh, okay.
Like, the kernel offsets?
**Michele Mancioppi** 34:04 Yeah, because we were using the, process attach and process detached syscodes.
to, find out the PAD, By PID, which signal killed the process?
And that is what we're using eBPF for.
And we had a way of finding it out, a bootstrap of DBPF sensor.
But I didn't write it, so I no longer… I don't know how it exactly worked.
**Nikola Grcevski @ Grafana / OpenTelemetry** 34:34 Yeah, it's difficult to know, like, if they… they don't move a lot, but sometimes they do move. Let's say if you're taking a look inside of a task structure or something, and which offset is the field, whatever, to pull the inode number or something, and it's… yeah.
**Michele Mancioppi** 34:50 But if you're curious, I know who wrote it at Instant, and I could give you the contact. He's now an engineering manager at Platform Engineering.
They are trying to do something better than Terraform.
**Nikola Grcevski @ Grafana / OpenTelemetry** 35:02 Nice.
Cool.
Yeah?
I'll be happy to chat, if there's a way to support older We've gotten requests to support kernel 5.4, Yeah.
That's, like, low on the list.
**Jack Berg** 35:30 Any other topics?
**Bastian Krol** 35:37 Not from my end.
**Michele Mancioppi** 35:39 Did your folks go and vote on when the packaging should take place?
If you're interested in following along.
We were settling for Wednesdays.
But then, that would have overlapped with UBI, and since They're very, very related.
We have been looking for another spot.
So if you have opinions on the matter on the community PR, Antoine is trying to hurt cats around that.
**Jack Berg** 36:11 Take a look.
**Bastian Krol** 36:16 Okay.
**Jack Berg** 36:18 Alright, everyone, take care, see you next time.
**Michele Mancioppi** 36:20 Bye for you.
**Bastian Krol** 36:21 Until the next time, bye-bye.
