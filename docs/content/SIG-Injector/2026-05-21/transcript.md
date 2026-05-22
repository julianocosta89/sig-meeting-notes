SIG: SIG Injector
Date: 2026-05-21
Duration: 42 minutes
Zoom Recording URL: https://zoom.us/rec/share/Dq-iXuTB099itr-3q50MSPpiPj6ic6ip4QelfOlUHyfW_BcdExDGFk_lp2RgYcE.rSJcThgh_EXXqFjr
============================================================

## Zoom Recording Transcript

**Michele Mancioppi** 02:16 Bastille.
**Bastian Krol** 02:20 Michaela.
**Michele Mancioppi** 02:23 What up?
**Bastian Krol** 02:26 Nothing much.
**Michele Mancioppi** 02:29 That's usually not bad.
**Nikola Grcevski @ Grafana / OpenTelemetry** 02:32 Okay?
**Bastian Krol** 02:34 Hey.
**Michele Mancioppi** 03:05 We have… Three issues.
Oh, we spoke a lot of those times.
**Bastian Krol** 03:20 I mean, they have a lot more issues than 3.
**Michele Mancioppi** 03:24 Sorry, I meant PRs.
**Bastian Krol** 03:26 Yeah, yeah, yeah.
So I think the PRs are not really something for discussion. I put one thing on the agenda, which is the first PR, or so the first issue in the list?
I'm not sure if Jack is joining today, that would be interesting to include.
**Nikola Grcevski @ Grafana / OpenTelemetry** 03:48 I can ping him. Ask him.
Good time.
**atoulme** 03:51 Hey, you wanna…
**Bastian Krol** 03:52 Yeah.
**atoulme** 03:53 You wanna kick out that, note-taker?
No?
**Bastian Krol** 03:59 Sorry, what was the question? Whose account is that? It's not mine.
**atoulme** 04:04 Yeah, something's taking notes. There's an AI note-taker when we see them in meetings with…
**Michele Mancioppi** 04:09 I'll take it out.
**Bastian Krol** 04:12 Yeah, let's… let's maybe kick it.
**atoulme** 04:15 How do I do that?
**Bastian Krol** 04:16 I mean, I guess it's from Joey from AutoAI? That would be my guess.
**atoulme** 04:21 learning.
But…
**Bastian Krol** 04:27 There's been a bit of discussion in the, I think in the maintainer's channel about these things, I'm not bothered by them, it's not nothing… Private, what we discuss here, but, yeah, fine.
**atoulme** 04:41 We already record those things, there's a… so the reason not to do that is because all those recordings that we make available are available in some form that we would like to control, and it's all public, but you can't…
**Michele Mancioppi** 04:54 I apologize.
**atoulme** 04:55 Just, add your own thing.
**Bastian Krol** 04:57 Yep, that's, that's, that's fair.
**atoulme** 05:00 Okay.
**Bastian Krol** 05:02 Okay.
Hey, thanks for joining.
**Sharing right now, I'm clicking around… Nikola Grcevski @ Grafana / OpenTelemetry** 05:14 Yeah, we can see it.
**Bastian Krol** 05:16 No, no, I was just asking who. That's fine, I mean… So, that's one thing I put in the agenda, we can as well start with it. I guess. I think there were no other things on the agenda, at least until 3 minutes ago. That's one bug that we noticed when we wanted to upgrade to, 080 in the zero repository, and we have a couple more tests there that test our whole auto-instrumentation image, and that, of course, includes the injector, and so that surfaced there, and it's a bug with that reason, recently introduced, libc detection fallback, that you did for for Red Hat, for older Red Hat distributions, and also Deeben Bullseye and stuff like that.
So we have an integration test for that here in the injector repo, which is a rather small C application, I think, so that works fine. It apparently breaks at least with Node.js when the executable is Node.js.
And it breaks in a not-so-nice fashion, so it, Finds the symbols, and it actually also does the set ends correctly, but when it reads the existing environment variables, it will always read, empty environment variables, even if the environment variable was set. So, like, the mechanism to… append or append to node options no longer works, it just destroys the pre-existing node options and only leaves the minus minus require in place.
similar for auto resource attributes, so we just clobber everything that was there before, which is not great.
I did a little bit of… or actually, my colleague Petra did a little bit of analysis with, with, Claude there, and that… I've pasted that into the issue, it sounds legit, so there are some copy… relocations involved that the linker does, which is a very strong argument for the original strategy with DLSIM that Mikhail came up with, so… That's good that we have that on the normal path, and we don't do that.
And for function symbols, that seems to be fine, but, for example, if the executable in question has a dependency directly on the Environ, Pointer that can then be somewhere else.
in the actual executable, and we get a pointer, we find the symbol, but it's not the right place in memory. And then, of course, that is already nulled, and we only read null from it, and that's a bit…
**Michele Mancioppi** 08:29 Yeah, exactly. Those are the bloody locations that I had looked at and went, nope.
**Bastian Krol** 08:37 Yeah.
**Jack Berg** 08:38 So… So, is this just, not just, is it… Is it that the fallback… It's not that the detection is broken, it's just that the behavior of the injector is broken when we use this fallback mechanism.
**Michele Mancioppi** 08:56 The.
**Bastian Krol** 08:59 Find the wrong address of Environ.
I think.
**Michele Mancioppi** 09:06 It is… it is similar to a memory corrupt… corruption bug.
Similar, because we go and read a member location that is no longer valid, and as such, we go and overwrite stuff that we shouldn't.
**Bastian Krol** 09:19 I'm… so, I'm not sure if that is really 100% accurate. Could… could totally be. It doesn't seem like we read garbage.
From there.
**Michele Mancioppi** 09:30 I really desired out location, losing information.
**Bastian Krol** 09:34 Yeah, yeah, we lose information, and we also make the application that we inject into lose environment variables effectively, and that is, of course, not… Good.
**Jack Berg** 09:50 So how does that work? So, we're reading from the wrong pointer, and I think we're… we're ultimately going to write to the memory location that we are reading from.
**Michele Mancioppi** 10:00 No, we use the Saturn function.
**Nikola Grcevski @ Grafana / OpenTelemetry** 10:02 That end, yeah.
**Jack Berg** 10:03 We use that app.
**Michele Mancioppi** 10:04 I'm pumped.
**Bastian Krol** 10:05 We write the asset n, that is the symbol that we read directly via n we run, via a variable, basically, but we write via a function symbol, and that is fine.
So… Of course, I mean, that's maybe a bit early, I guess.
**Michele Mancioppi** 10:25 There's a solution for this. So, since function pointers do not seem to have a problem with relocations.
What we could do in that path, instead of looking for the Environ symbol, is to look for getEv. The reason why we're looking for the Environ symbol is that we need to know what is the pre-existing value of the environment for eyeballs that we can then append.
If instead of looking embryon and then lose a time, would you get time with denser time?
But kind of… there is… The reason why I didn't do it originally is because I thought there could be a situation where we needed to enumerate all the existing environment variables, but that is actually not the case in the logic of the internet, as far as I remember.
**Nikola Grcevski @ Grafana / OpenTelemetry** 11:09 I always look for a specific one, yeah. I don't do that.
**Michele Mancioppi** 11:12 get away with looking up GATAMP, and then have an input?
**Bastian Krol** 11:16 We could just always look up geten, independent of which path we end up, that would make it a little bit simpler, and I don't think we need to do that differently. That's one thing that I also thought about, just using.
**Michele Mancioppi** 11:31 It was a loose.
**Bastian Krol** 11:31 that then.
**Michele Mancioppi** 11:32 There was a reason why I did underscore, underscore embryon, and not Katanv.
**Bastian Krol** 11:37 I mean, the very original reason was that we wanted to hijack the symbol entirely.
**Michele Mancioppi** 11:44 No, I was, I actually thought about it when I did that huge reflection.
**Bastian Krol** 11:49 And you probably documented that somewhere, right?
**Michele Mancioppi** 11:52 Yeah, that probably is doing a lot of heavy lifting, whether it'.
I don't remember anymore.
**Bastian Krol** 12:01 Other things that we could also do, because we also have the constraint that we need to look up a couple of environment variables before we even look up symbols, we already read from procenv.
Before we do the… and we could just do that entirely for everything.
**Michele Mancioppi** 12:20 51.
**Bastian Krol** 12:21 Reach.
**Michele Mancioppi** 12:21 That is not true, because the, the injector runs… Between… so there is logic that happens before… The injector, so the init array starts, and the proc environ is the environment that the operating system uses to spawn the process, but any modification before the init array is not represented.
**Bastian Krol** 12:53 That's fair. I don't think there can be a lot of stuff running between that, but yeah, fair.
**Michele Mancioppi** 12:58 I also don't want to find out the hard way that there is.
**Bastian Krol** 13:06 I would say…
**Michele Mancioppi** 13:07 I would change it for now only in the fallback path.
Where, in that case, instead of looking up the Emron symbol, we took a temp.
**Jack Berg** 13:17 What?
**Michele Mancioppi** 13:17 And the path already works with the LCIM, I don't see why changing it.
**Jack Berg** 13:21 That seems reasonable, but it makes the code a little bit more complex, and path-dependent, and so I guess, what would it take for us to feel comfortable calling get and everywhere? Like, what kind of testing would we need to add to, you know, eliminate the risk?
**Michele Mancioppi** 13:38 Like, extensive field testing.
**Jack Berg** 13:40 Field testing.
**Michele Mancioppi** 13:41 You see it with this kind of stuff, Jack, right? I mean, you gave it to Red Hat, then the moment, like, we turn it on, Interzero rolls out to hundreds of customers, then bloop.
**Jack Berg** 13:54 Yeah, I know, I'm just, like, I'm just thinking, like, because we might be stuck with that forever, right? And, like, what would the field testing look like that allowed us to get comfortable? Because it's, like, this kind of esoteric code path that needs to be exercised to… to use getENV, and so…
**Michele Mancioppi** 14:10 I would say, we implement it this way, we put a nice feature flag.
And the moment that we… for example, in their stereo, we would stick with the current behavior with Environ.
Because others are great customers. The, the injector would do the get amp instead.
And then, hopefully, there is enough validation, and in a year from now, we can get rid of the… of the flag.
And consolidate, ideally, ink attempt.
**Jack Berg** 14:41 So, maybe the default behavior is getENV, getEnv, and the fallback of this flag is to use the, I don't know what… how do we pronounce this? Underscore, underscore, info.
**Michele Mancioppi** 14:56 envelopes can go.
**Jack Berg** 14:58 the envirin symbol, and so yeah, so everybody can… can get their… Can have a safe fallback for their operators without risking breaking their customers, but we can still sort of exercise this in a wide environment by default.
**Bastian Krol** 15:16 I, I, to be honest, I think, Michaelie, you worry too much. I would maybe just go with.
**Nikola Grcevski @ Grafana / OpenTelemetry** 15:22 Yeah.
**Bastian Krol** 15:23 And I don't… I don't see why… I mean, if it works across our test coverage, which is not super small, taking this repository and the des-zero implementation image test together, I would feel… Fine, actually, but…
**Michele Mancioppi** 15:41 But you also have to be the person that is going to answer those tickets on our site, for sure.
**Bastian Krol** 15:45 Sure, right? But, so… Nikola Grcevski @ Grafana / OpenTelemetry 15:47 Talk about it this way, you're already calling Satan.
So, calling getEnv should be… if setEnv works, getEnv should be actually… Right.
**Michele Mancioppi** 15:58 I am at that stage in life where I trust nothing.
**Bastian Krol** 16:02 Well, at some point, we also started with the current implementation without giving it wide field testing.
**Michele Mancioppi** 16:12 But these were times, there were a different time, where the tester operator was not used by hundreds of customers.
**Bastian Krol** 16:18 Yep.
**Michele Mancioppi** 16:19 Anyway, really innocent times.
**Bastian Krol** 16:23 I mean, that's… there can be different perspectives on all of that. I think the get-ins… Pa sounds very good, and sounds super reasonable.
Timeline-wise?
Do we just want… To revert the fallback first, push out a release, then implement the fix, or do we just go straight to the… Pix with getN…
**Michele Mancioppi** 16:53 I mean, why would we revert? It was already not working for Red Hat. Now it doesn't work in a different way.
**Bastian Krol** 16:59 Yeah, but, it just did nothing. It did not inject for these older distributions, and that was… Better than the current behavior, I think. But I mean, I don't have strong opinion. We can… the latest version is broken for these VDO distributions.
**Michele Mancioppi** 17:21 Oh, I, I remember, I remember why, I remember why I went with, Environ instead of GetAv.
And that is because I was wary of tree shaking.
I thought that in some embedded scenarios, the, the lip-sy could be cut down to remove, to remove symbols it didn't need.
And, when you look at, for example, what Java does, like, there is a part of the JVM that is, actually uses GitM, and then in the SDK, in the JDK, the JDK, the, system.getenv actually goes and reads the ambulance symbol.
**Bastian Krol** 18:05 wait a second… we only work for dynamically linked libraries which link to Ellipsei. How would tree shaking in the.
**Michele Mancioppi** 18:14 Yeah, Zico.
**Bastian Krol** 18:15 post.
**Michele Mancioppi** 18:15 Under lip-sync.
But it was, the reason why I did it, it was out of a characteristic overabundance of caution on my side. I don't think that… If the decision is we use Environment, we use GetEnv.
My argument for not using a temp holds water, right?
But at least I remember why I did it.
**Bastian Krol** 18:38 Okay, okay.
**Michele Mancioppi** 18:40 Because the ambulance symbol must exist.
But in some…
**Bastian Krol** 18:44 Right, because it's politics, or…
**Michele Mancioppi** 18:47 Yeah, because that's… like, everybody reads Environ. The Python uses… reads the Environ symbol. The JDK uses the GRE, sorry, that uses the ambulance symbol. If that doesn't exist, then goodbye. There is nothing we can do.
**Jack Berg** 19:04 Well…
**Michele Mancioppi** 19:04 At CATM is not so guaranteed.
**Jack Berg** 19:06 Well, so actually, so let's think about that then. So, if the only places where we think get N… will not be available are these, like, low-level embedded systems that might have done tree shaking, then it's probably not going to be the case for any of the, you know, high-level applications that we're trying to instrument, and so we can use the absence of GETENV as just, like, an exit early, a short circuit.
**Nikola Grcevski @ Grafana / OpenTelemetry** 19:30 bars go to, even…
**Michele Mancioppi** 19:31 I said that my argument doesn't hold water.
**Jack Berg** 19:34 Oh, okay, I see.
**Michele Mancioppi** 19:35 Overabundance of caution.
**Jack Berg** 19:36 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 19:37 Yeah. And then maybe you could say the same thing, like, tree shaking could have removed sedan, and then you can't call it.
**Michele Mancioppi** 19:43 Yeah, exactly, but the point is, like, the likelihood was, like, if I can use a symbol and a function instead of two functions, I'll go with the… without symbol, nothing works. Neither ZATAM nor get temp, and that's why I said, let's add the minimum amount of obvious dependencies.
**Jack Berg** 20:00 Okay, so let's, okay, so that's good, that's great context. And, so let's say we come across a process, and it doesn't have getEnd, and what do we do? We want to exit early, but do we also log, and at what severity level?
I would say debug level severity, because this is, like.
you know, this is something that is… we don't want to create that noise, right? That was why I opened this, this RHEL issue originally, is because we were getting this noise on all these, just things like grep and, these other processes that were running that are… were linked to old versions of glibc.
And, so yeah, what do you guys think about that? Just, like, you know, having it be a debug or trace-level log that you have to, like, you can see if you opt into it, but, like, otherwise it's just gonna silently exit early?
**Michele Mancioppi** 20:50 this was, litigated a lot, both in Cider Zero and then in the, in, in the SIG. There is no good… no good solution, there is just a less annoying solution with more false negatives. So, if we go with debug, then the customer just doesn't see applications, and then they need to know that that was supposed to be monitored, and it's not.
If we go with being annoying and posting a lot of logs, then everybody's annoyed.
It's… at the end of the day, we went with the… False negative, so if the injector cannot inject, then we… we shut up unless you go in debug mode, but…
**Bastian Krol** 21:36 Smart.
**Michele Mancioppi** 21:37 It was…
**Bastian Krol** 21:37 Currently, when the injector cannot inject, I think we lock a warning that is always locked by default for the most error cases.
Wait a second, now the default error level… the default doctor level is error… or maybe I'm wrong? I'm not sure. Okay, I'm not sure.
**Michele Mancioppi** 21:56 I'm pretty sure that we… pretty sure, I mean, you put me in a Zoom room and talked at me for several minutes on the matter until I acquiesced.
**Bastian Krol** 22:05 Yeah, yeah, yeah, that's right.
That sounds familiar. Could have happened.
**Michele Mancioppi** 22:11 It rings a bell, right?
**Jack Berg** 22:13 So, like, the question is, is these one of those error cases that you need to be loud about? And I think the answer is no.
**Michele Mancioppi** 22:20 No, it's the same thing as there is a dynamically linked process.
Which, however, doesn't link to libc. That's the same amount of stuff.
Like, maybe we could be a bit louder if we happen to find such a time and not get timed, then it's… like, what the fuck?
But, like, hey, I don't find the functions, I don't find any of the functions I need, then I cannot inject, that's fine.
**Jack Berg** 22:44 That's a good question. What do we do if we don't find set env? Because tree shaking might similarly, like, not include setEMV, and would we… we would have seen that, too, as well, right?
**Michele Mancioppi** 22:55 Yeah, no, but as I said, the tree shaking was a completely theoretical thing I had in my head. I've never seen it in practice. I know that Particular embedded systems that use for some things like Yocta could have done it. I don't believe that anybody would use OpenTelemetry to automatically inject stuff into those applications.
**Jack Berg** 23:15 Okay. But, you know, I guess my point is that, though, that in your theoretical concern, set EMV might be tree shaken as well.
**Michele Mancioppi** 23:24 Yeah, of course.
**Jack Berg** 23:26 Right? But we don't have any protection for that.
**Michele Mancioppi** 23:28 And today.
**Bastian Krol** 23:29 Well, yeah, I mean, if you find… we only inject if you find both symbols, or all the symbols we need, so that… that is fine, I think.
**Jack Berg** 23:36 Okay.
**Bastian Krol** 23:37 That seems like a fun place.
**Jack Berg** 23:38 Like, expect these symbols, and if they're not there, fail silently, and turn on debug logging if you want to see more details.
**Bastian Krol** 23:45 I think for the lock level, we should just do what we do right now for these error cases, and I think we lock all of them at level warning, and the default lock level is error, so they are silent by default, and you… So, I think debug is a little… very fine game for an error condition, but, since it.
**Jack Berg** 24:07 As long as it's not on by default, that's all that.
**Bastian Krol** 24:09 Yeah, yeah, yeah, I know, I know, that's what you meant, that's exactly right.
**Jack Berg** 24:14 Okay, so I think that we should roll forward with this, rather than reverting. Do we all agree now that we've sort of Recounted the history of how we got here?
**Bastian Krol** 24:26 Yeah, I think the only reason for reverting first would be if you say, well, nobody from us has time to work on that fixed in the next two months, and we don't want to leave that slightly broken version as latest published. If we can fix this in the next few weeks, I think that's fine with not reverting.
**Jack Berg** 24:49 I can… since this is, like, something I introduced, I can take care of the fix for this, and Either today or tomorrow, I'll have a PR.
**Bastian Krol** 24:58 No, we, we… there's not… no rush like this, so it's fine.
Lovely.
I tried to document the decisions in, the agenda document. Did we now have a consensus on whether we do get N for both branches?
Yeah, okay.
**Michele Mancioppi** 25:28 With, with, place the possibility to… to fall back on the, on the current behavior?
But honestly, I mean, the likelihood that we don't find Gattan with ELCM, to find Environ, I mean…
**Jack Berg** 25:41 No, it's two things. It's, like, the likelihood that we don't find Get ENV, and that we're also in the context of instrumenting a process that tree shook GetENV. And so that's, like… and would actually be instrumented by this thing. I don't think that those conditions exist. I think that if we find that they exist, we go at a fallback later.
**Michele Mancioppi** 26:01 Yeah. Yeah, okay, I'm fine with that.
Cool. Yeah, I'm always super extra cautious about, about, this kind of things in the injector, because the impact of Failing to instrument something.
tends to be, really difficult to be spotted. And the breach of trust, given the fact that it's dark magic.
is higher than normal other bugs, and this has colored a lot of the way that I built the original injector, and I go about having opinions about how to evolve it.
**Jack Berg** 26:39 Makes sense.
**Michele Mancioppi** 26:45 Everybody loves Futu when it works as intended.
**atoulme** 26:50 Maybe that's a discussion we're not having, is that maybe the injector should start to have internal telemetry.
**Michele Mancioppi** 26:57 That is, I thought about it, and technically there is a ZIG SDK, but the point is, the same amount of annoyance that you get with the injector logging to standard output or standard error, you have with the injector sending a message of a new TLP log bridge.
Same amount of annoyance at the end of the day.
**Bastian Krol** 27:16 And making a network connection in the LDP low talk there, it sounds…
**Michele Mancioppi** 27:22 Yeah, that's not… that's not… That's not…
**Jack Berg** 27:26 Log-based telemetry.
Log-based telemetry, that's what we're limited to.
**Nikola Grcevski @ Grafana / OpenTelemetry** 27:31 Yeah, Prometheus.
**Michele Mancioppi** 27:32 Not even log-based, just standard output and standard error.
**atoulme** 27:38 Yeah.
Just… But maybe there's… we will really take this nigger.
Anyway… I do have.
**Michele Mancioppi** 27:48 12-factor apps, but on steroids, are the limitations we have.
**atoulme** 27:53 Yeah.
Anyway, onwards, right? We have… it's… thank you for going waddling through all this.
I do have an action item I wanted to kind of go to. If we're good with this one, there's… A thing I wanted to bring up… So… in December… Jack, you initialized a change, which is that… We would like to make sure that, NVAR injection only supports keys that start with hotel underscore.
I think that's perfectly fine, but it limits the ability for vendors like us to adopt the injector, because we would like to… We have some features that we are controlling via environment variables.
We would like to make it easy for us to move to that. We don't like… we don't have that capability right now.
**Michele Mancioppi** 28:50 Wait, I'm sorry, I'm missing the context. Why?
As a vendor, you cannot control variables in notar underscore.
**atoulme** 28:58 Yeah, take a look at the doc.
Let me see here… Probably in the chat. I can share my screen, but that's gonna be big.
Jesus. So… There's… there's a… There are some good points, right? The injector can become a natural attack vector for those looking to expose vulnerabilities.
So by default, we should not just, let people inject whatever.
And so we should limit to suit key starting with hotel underscore.
**Michele Mancioppi** 29:34 Okay, now I understand it.
**atoulme** 29:37 But, I mean, we have things that also start with Splunk underscore.
**Bastian Krol** 29:40 Yeah.
**atoulme** 29:41 Are we having just…
**Bastian Krol** 29:42 Add a few more prefixes to the allow list.
**atoulme** 29:45 Yeah, can we… is that configurable?
**Bastian Krol** 29:48 No, it's not. I mean, we… making it configurable would defeat the purpose. I was thinking of.
**Michele Mancioppi** 29:53 Okay.
**Bastian Krol** 29:54 hardcode a few allowed prefixes, like Splunk underscore, OT underscore, it's all hard-coded, but…
**Michele Mancioppi** 30:00 Technically, I mean, the Splunk could work, and have that small patch set.
If the concern is security, then the correct way is to fork.
**atoulme** 30:12 You're right. So…
**Jack Berg** 30:16 Thin fork, though, not fat fork, just a thin fork.
**Michele Mancioppi** 30:19 Yeah, very thin. Just one small, tiny wee patch that.
But hopefully as muttering of tests.
By the way, I took that into account, when, with the meta-architecture for the packages, making most of the injector packs walkable.
**atoulme** 30:37 Yeah.
Yeah, that makes sense.
**Michele Mancioppi** 30:46 If we start putting more prefixes here, then this will become, over time, an archaeological track record of observability companies.
That's not great.
**atoulme** 30:59 I don't want that teaser, right? And frankly, we should catch the caboose in… over from having any extensions require a CRF configuration like that, I don't like it.
But that's not… that's not something you can do. Would there be a middle ground here where we can compile the source with a flag that would allow us to override the default list?
**Michele Mancioppi** 31:21 That would be an option. Another option would be to expose a symbol with the allowed…
**atoulme** 31:27 Yeah.
**Michele Mancioppi** 31:27 No, if we expose a symbol with allowed prefixes, then an attacker can modify the symbol. So, no, that will be a compiler flag, yeah.
**atoulme** 31:36 Yeah.
**Bastian Krol** 31:37 That's on Coach.
**atoulme** 31:37 compiler flag, it's maybe less expensive for, like, in terms of having to maintain a fork, I can see.
**Michele Mancioppi** 31:43 Yeah, yeah, yeah.
**atoulme** 31:44 Hang on.
**Bastian Krol** 31:44 It's a good idea. I like it.
**atoulme** 31:46 Okay. Alright.
Okay, I got a path forward, thank you. I'll put that in the notes of the meeting, and then,
**Bastian Krol** 31:52 Yeah, it should probably be a compiler flag with a list, because you still want to allow auto underscore prefix in addition to Splunk underscore, would be my guess.
**atoulme** 32:02 Yes.
**Michele Mancioppi** 32:02 We make the full list of allotridences.
**atoulme** 32:05 Use a compa flag.
To override that.
We'll see you.
**Jack Berg** 32:11 I'll just note, while we're on this topic, is that, you know, the usage of vendor-specific environment variables is going to diminish as declarative config picks up, because declarative config, you have a single environment variable that points to your file, and within that file, there's accommodations for vendor-specific distribution settings.
**Bastian Krol** 32:33 Nice.
**Jack Berg** 32:34 So, yeah, this is probably just, like, a temporary artifact as we're… Maybe not… yeah, I see you're shaking your head.
**Michele Mancioppi** 32:41 It's refreshing. Your optimism is refreshing. I see why you're saying that. I want to see that day.
**atoulme** 32:49 We are working towards this.
**Jack Berg** 32:52 Working towards this.
**Michele Mancioppi** 32:54 Apotically.
**atoulme** 32:55 Yeah, one more reason not to spend too much time on trying to make something bend backwards and meet whatever, right? So, I'm okay with compiling the injector with a flag, or doing some wheel.
**Michele Mancioppi** 33:07 Yeah, because anyhow, you're building your own container images.
**atoulme** 33:10 right now… think… we have a spike that I built, where I just download the release of the injector.
So… By the way, we do not sign our releases, do we?
**Michele Mancioppi** 33:25 No, I don't think we do.
**atoulme** 33:28 We shouldn't.
**Bastian Krol** 33:29 Good question.
Do we… maybe we already have a ticket for doing that, or maybe not?
No, we don't.
**Jack Berg** 33:39 Does it matter, since we don't publish them anywhere? .
**Bastian Krol** 33:43 The artifacts on GitHub with the Reese's?
**Jack Berg** 33:47 Yeah, just there, I mean, like, you know.
So, you know, if you're… if we only publish it to releases, then in your… the install flow is for you to download it from releases. Like, where is the… the man-in-the-middle type of attack that could, cause somebody to tamper with us?
**Michele Mancioppi** 34:05 I mean, GitHub doesn't have the greatest reliability or security track record recently.
**atoulme** 34:11 Yeah, I mean, there is a message that I posted to the leads channel, I think it's fairly common as known. As of two days ago, GitHub has been investigating that their internal repositories have been breached.
**Jack Berg** 34:22 Well, but consider that. So, like, if you can breach GitHub and publish a new artifact that gets downloaded from the releases link, then you can also similarly publish, you know, the attestation, the signature of that artifact to that same location, like a modified signature.
**Michele Mancioppi** 34:40 I usually have the private key, yes, but…
**atoulme** 34:42 But they don't, right?
**Michele Mancioppi** 34:43 The ears on the same.
**Jack Berg** 34:46 The key isn't the same. Okay, so…
**atoulme** 34:48 you can verify with your key, right? If you don't have… if they change your keys.
**Jack Berg** 34:52 Okay.
**atoulme** 34:53 If you somehow have access to a private key, you're right, game over. But in that case… Like, have bigger problems, right?
**Jack Berg** 35:01 But, like, what would even be the standard way for you to… for us to publish the signatures next to those artifacts? And, like, you know, the standard would have to… it would have to be standard in such a way that, like, common tooling could download both and verify.
**Michele Mancioppi** 35:15 Make me use the PGP word.
**atoulme** 35:17 Look, I mean, in our own releases, right, what we do is we publish an additional file, calls the .ac file, that goes with the… it's just suffixed to what we publish.
Let me share my screen.
So, for example, we're going to make available a zip file. Well, we're going to make an ASC file next to it available.
I think we also have the digests in… we had the checksums also someplace. I think there might be a checksum as well. Yeah, TXT here.
So… Yes, the signature file is separate and next to it. In some cases, like the MSI, it will allow you to sign and update in place the exit file with the signature embedded into it.
Okay. So, when possible, we do that.
And, you know, yes, you're right, this is not foolproof, it's not the end of the road, but we do not currently sign. Maybe, also, the answer is, hey, we should not be publishing binaries on a GitHub release. And, you know, we're a very nimble, small project. If you're going to do this, just download and build from the tag.
Don't trust us.
**Michele Mancioppi** 36:27 What you're saying, Antoine, I would feel entitled to do only when there are system packages of decent quality.
And the injector and the operator.
**atoulme** 36:39 Yeah, that's okay. Yeah, we don't have to do this now, I'm just… sorry, I'm just asking a question, I'm not saying.
**Jack Berg** 36:44 Yeah.
**atoulme** 36:44 oh my god, we don't have this. I'm sorry, if you would.
**Jack Berg** 36:47 No, no, no, no, I didn't take it that way, I was just having… continuing, like, the line of thinking, yeah, of how this might actually work.
**atoulme** 36:53 But it's like defense in depth, right? You keep adding more and more of those type of mechanisms, the day something unfortunate happens, then at least you have this to back up yourself with, like… You can go back and check.
**Bastian Krol** 37:07 I also don't see too many downsides with signing them, except for that somebody has to implement that in the CI.
Workflow, but… That's…
**atoulme** 37:19 Yo.
**Bastian Krol** 37:19 Sounds good.
**atoulme** 37:20 The collector does it using a bot, so it's not actually using any human time. There's nobody who has to enter a passphrase or anything like that.
**Bastian Krol** 37:31 No. I mean, we need to implement it in our GitHub action, and that's all the investment it takes, and that's not rocket science, I guess.
**atoulme** 37:41 Because I popped that up, I'm happy to open an issue about it, but we don't have to work on this.
That sounds good.
**Bastian Krol** 37:47 That's good. Throw it on the pile.
**atoulme** 37:50 Yep.
I'm sure we'll find some new grad who wants to make bones, who wants to grow.
**Jack Berg** 37:55 Summer of Code. Summer of Signing.
**atoulme** 37:57 I'm phoning.
**Michele Mancioppi** 37:59 Yeah, but the point is that somebody needs then to understand, and if there is something that the security industry has succeeded in doing.
It's piling a lot of complexities that make my head shake.
**atoulme** 38:12 That is fair, but that could also be the job. It's like, you can reject the change and say, I'm sorry, document, make sure it's in line with what OpenTech wants to do, and I certainly don't want science experiments in the middle of my XTI.
It's… we can push back.
And then either it helps or it doesn't, right?
**Michele Mancioppi** 38:34 I mean, Antoine, if you want to have fun with signing, I have in the right SIG, and it's not this one.
**atoulme** 38:41 It's coming up, yeah, I agree.
**Michele Mancioppi** 38:43 It already came up.
Lastly, you were just not there.
**atoulme** 38:47 Oh, man, I missed one meeting.
**Michele Mancioppi** 38:50 Which was a terrible mistake.
**atoulme** 38:55 But signing… signing packages makes total sense. Like, yeah, yeah, no.
**Michele Mancioppi** 38:58 You're not able to consume packages that are not signed unless the other side has a set of world-level security. It's just…
**Jack Berg** 39:07 Yeah, no, my… I totally agree with all that. I just was wondering, because, like, you know, how this intersects with us trying to publish to, you know, artifact repositories, rather than just publishing to, you know, GitHub.
have… but I think they're unrelated things. I think, you know, they're… Proceed with signing while we do GitHub releases, and then independently pursue publishing elsewhere.
**Bastian Krol** 39:31 Yeah, and also, I mean, just for the binaries, I think doing it with GitHub is really fine, and there are consumers that don't want system packages, but just the binaries, like my operator or our operator, and… So…
**Michele Mancioppi** 39:51 But then there, I mean, we would be perfectly fine adding the build process to our container image. The same thing Antoine will need to do for the custom.
**Bastian Krol** 39:59 Sure, yeah, we can do that as well.
**Michele Mancioppi** 40:04 I mean, the biggest annoyance there is to have to pin also in our… in our build infrastructure the zinc version.
**atoulme** 40:11 Mmm.
It's not pinned.
**Bastian Krol** 40:16 Thanks.
**Jack Berg** 40:16 Like, who would ultimately ever consume these binaries directly? Like, vendors are going to… Have to have a build process where they could build them from source, The operator one day.
**Bastian Krol** 40:29 literally…
**atoulme** 40:31 I tried to use the .SO file, and it worked okay for my spike. It just… I'm falling… I'm falling on my sword with the Envar built… built flag now, but…
**Michele Mancioppi** 40:41 Yes, but come on, Antoine, I mean, the level of very specialized knowledge that you need to have to just get the naked assault file, and make it do something useful.
**atoulme** 40:52 Oh, yeah, yeah, no, only vendors would be interested in this, and they would inject that into something that they own, and it would be part of a bigger package.
**Bastian Krol** 40:58 Yes.
**atoulme** 40:59 Yeah, yeah, yeah, definitely. We're in complete agreement, but I would say that the .a so far served me in that particular use case, rather than building from source.
Eventually, I'd love to not have to build anything from source, and just use the standard injector package.
Anyway, I've… I've opened an issue.
I'll just put a note in the docs to that, sidebar.
Go ahead.
**Jack Berg** 41:34 Yeah, you got it.
**atoulme** 41:35 Sorry. Sorry, Jack.
Okay, sidebar… On signing.
Lower priority.
Okay.
That's it. All set here. You have anything else, folks?
**Michele Mancioppi** 42:00 No, if anything, I can say that… Or the kind of mind-numbing complexity that the injector has to deal with.
I think we have a… Pretty low rate of change, and a very low rate of surprises.
It pleases me.
**atoulme** 42:19 Good.
**Jack Berg** 42:19 It should be a small program, so it should have a proportionally small change rate.
**Michele Mancioppi** 42:24 A small program with a lot of packed in knowledge, and that never bodes well.
**Jack Berg** 42:30 It needs to run really fast, and a lot of times.
**Michele Mancioppi** 42:34 And doing on a bunch of binaries that we have never seen and we will never see with optimizations we couldn't even possibly imagine.
**Jack Berg** 42:44 So far, so good.
**Michele Mancioppi** 42:46 The linear injector that could.
**atoulme** 42:50 Awesome.
I'm off. Thanks, folks. Take care.
**Bastian Krol** 42:54 I…
