SIG: Python SIG
Date: 2026-10-22
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 00:37 Hey, everyone.
**Tammy Baylis** 00:43 Riccardo Li Lukas.
Hey, everyone! Welcome back to the OTELPython SIG meeting.
Meeting notes that you see on the screen are also linked in the chat. And let's start with some triage till about 9-10, which I'll do. And yeah, as always, feel free to add topics you'd like to discuss, to this list.
Below for today's agenda.
Cool, so we've got our… Bought managed triage boards here.
Oh, sorry, one second, I'm in the wrong account.
Whoops.
I'm sharing for one second.
Just gonna switch accounts… And, try sharing again. Pull request dashboard… Make my screen big again, there we go.
Sorry about that, so… This is our… Let's look at our core board.
What's waiting on reviewers?
Mmm, we won't go over bots.
Okay, new one from Lukas, SDK Enforced metric cardinality limits.
Which is in the spec.
And in the declarative config.
Yeah.
**Lukas Hering** 03:58 I had, I had, Codex go through the declarative config and found a bunch of gaps, so I just opened a few PRs.
This one's actually even broader than just declarative config, though.
**Tammy Baylis** 04:15 Right.
**Lukas Hering** 04:16 Ever had this, like, So, yeah, just general cardinality limit in metrics.
**Tammy Baylis** 04:27 Yeah, thank you. Thank you, Codex.
We'll have to take a look at that.
Lukas is this one… And this is not about metrics, but span and logs.
Oh, approved, thank you, Leighton.
And more… Sounds similar.
Ready?
Spicy Shark Co. Re-initialized metrics locks in a fork jello. Forks are so hard, okay.
We have a linked issue, thank you for that.
Okay, I think this is worth a look.
Hmm… Thank you for that.
Declarative config with NVAR parsing as per spec.
Yeah, that's important. Thank you.
**Lukas Hering** 05:40 Yeah, it is,
**Tammy Baylis** 05:41 Oh, sorry.
**Lukas Hering** 05:42 Oh yeah, I was just saying, there's a… there's a few bugs.
**Tammy Baylis** 05:53 Cool.
Multispan… multi-span processor?
We're having refuse already.
Thank you for those.
Right, we gotta… Have another look, but… Already gone through, thank you.
3 more minutes… Inline utilty type annotations and stale.pyristoga.
linked issue, thank you, God. Oh, thanks, Dylan.
Okay, so there's… Oh, no. That's in Pydantic, not in a hotel I just mentioned.
Logs enabled filtering.
Thank you for issue.
Already being reviewed… Doesn't need fixes.
Yeah.
CLA now signed… Fuzz. Add trace state fuzzing target using Oh, interesting.
**Lukas Hering** 07:56 Oh yeah, this was one, actually, I was gonna maybe bring up, but, I… I felt like we could maybe… maybe add some… add some fuzzing just for, like, most of the propagators and stuff. There's also the, in doing this, I think… I forgot what the… there's, like, the open source, badges, I guess, that we'll get for doing this. I think, long term, I also want to add this to OSS fuzz, so, like, it'll just run… Continuously for us, but, yeah, so I just added these for… it's just for trace state, Yeah, basically just tests.
bunch of different random inputs. I used… yeah, there's, like, a manually generated, or a, A grammar… with… yeah, it uses Lark to… as, like, kind of an oracle, for… Comparing stuff, but… Yeah, just thought, maybe we can add this, since, I think there's been a few bugs with, like, some of our propagators, Yeah, so…
**Tammy Baylis** 09:10 They're awesome.
**Lukas Hering** 09:12 And, or has more experience with fuzzing, and if there's a better way to do this.
**Aaron Abbott (Google LLC)** 09:21 Yeah, super cool.
Is this just… we're still just in the triage, right?
**Tammy Baylis** 09:29 Yes.
**Lukas Hering** 09:29 Yeah, okay.
**Tammy Baylis** 09:30 Yeah, I'm…
**Lukas Hering** 09:31 I can add it to the topic, so if you want.
**Aaron Abbott (Google LLC)** 09:33 Yeah, yeah, I was gonna say something, maybe we could add it to the topics.
**Tammy Baylis** 09:37 Yeah.
And, time's up, so we'll stop triage.
Can copy that if we haven't done that already.
Great.
Okay, 9-10, let's go to our regular topics.
What we're working on this week, well, we're all looking at PRs, that's for sure.
Riccardo announcement.
**Riccardo Magliocchetti** 10:12 Yeah, like, next week, there will be, like, a GC… Governance Committee elections.
And every member of Open Elementary, Captain Bot?
And so… Take a look at the candidates, their proposals.
And, if you can vote.
And you won't.
Remember to vote next week.
Let's see.
**Tammy Baylis** 10:48 Awesome, thank you.
Yeah, vote, it makes a difference. Next… PR, or topic PR, Emidio.
Take it away.
**Emídio Neto** 11:04 Hey.
Yeah, I know we have discussed this before, but just bring it here for due diligence, Just for context.
This is related to the log instrument, or… When you have the trace context injection enabled.
And, logging handler is adding, The log instrument residing, hotel trace ID, hotel span ID, and trace sample attributes.
And so those attributes are also getting exported.
We need to payload, like, to the collector, or wherever.
The main use case for us, like, in Python is to have these attributes for formatting console or file logs.
But I don't see so much benefit of having it getting exported, and… This PR is… It's fixing this, by removing the duplicated attributes.
So I just wanted to bring here to see if anyone eats.
Against, to remove that application.
During the export of, of the log hackers.
I mean, remove the duplicated attributes.
You got that room.
**Aaron Abbott (Google LLC)** 12:25 Yeah, so does this… Does this apply only when it's using, like, the hotel logs SDK to remove this stuff?
**Emídio Neto** 12:35 Mainly when you set the… when you are using Log Instrumenter.
And you set the perimeter of, Inject, trace context, something like that.
And you get those attributes.
During the Log Instrument, or…
**Aaron Abbott (Google LLC)** 12:55 Oh, so there's… there's a new config, or, like, does it stop duplicating them? Sorry, maybe I'll just say what I'm… what I mean is, like,
**Emídio Neto** 13:03 You can… you can, disable that, but when you enable, you get RTPs duplicated.
**Aaron Abbott (Google LLC)** 13:11 Okay.
**Emídio Neto** 13:11 The main use case for users to enable that is to get into, formatters.
For, you know, getting the information on the logs.
But, sorry, go ahead.
**Aaron Abbott (Google LLC)** 13:30 Can you say that last part one more time? Sorry. I think we're probably saying the same thing, but the main use case is to keep it when they're not using the logging SDK.
**Emídio Neto** 13:42 Yeah, and you… you need to format the logs your application is outputting, like… But it also is getting… this also is getting exported, you know, in the preload.
Yeah. That's duplicated attributes, so… With this PR, you can still have the attributes available for martyrs.
But, When we create a log hack code, it's not getting passed through.
So, we looked at.
**Aaron Abbott (Google LLC)** 14:16 So this…
**Emídio Neto** 14:16 Is that the…
**Aaron Abbott (Google LLC)** 14:19 Okay, cool. So this preserves the behavior, like, where people aren't… if they're just using, like, standard… standard library logging in Python and, say, like, tracing, but they don't care about the logs SDK, they can still enrich the… standard library log record with the hotel attributes, right?
**Emídio Neto** 14:37 Yup.
**Aaron Abbott (Google LLC)** 14:39 Cool.
**Emídio Neto** 14:46 Yeah, I know we discussed that before, but we didn't have a decision about it.
I believe one or two.
Two times we discussed that, but… Since now we have a PR.
So I would like to get this in, if anyone is… I guess.
**Aaron Abbott (Google LLC)** 15:02 Does it change the default behavior?
**Emídio Neto** 15:07 It took a break for users, which… I rely on those attributes for, like, let's say… dashboards, alerts, things like that, but I doubt, users are relying on this.
**Aaron Abbott (Google LLC)** 15:30 Okay, cool.
**Emídio Neto** 15:37 Cool. Yeah.
That's all for me. Thank you.
**Tammy Baylis** 15:46 Thanks, Emidio, and thanks for discussion. I've approved it.
Next topic, Lucas, PR579… oh, did I… yeah, 5797.
**Lukas Hering** 16:00 Yeah, I think there's… This is the same as Aaron's issue. If, Aaron, you just… we can just go over your topic, but…
**Aaron Abbott (Google LLC)** 16:09 Oh, yeah, yeah, yeah, it's the same thing.
Sorry about that.
Feel free to talk about this one.
**Lukas Hering** 16:19 Oh, you, you, you brought it up, you, you can go ahead.
**Aaron Abbott (Google LLC)** 16:22 Okay, yeah, at the risk of… you know, prematurely optimizing the, I was talking about this last week, but I was looking at things in our… before our stable release that would make it difficult to… Optimize later, and this was one of the things that came up.
And it's basically, we're using… a standard Python enum for the severity number.
Which doesn't create, like, a subclass of int, so it's kind of… Like a, like a wrapper around the int?
And… In practice, it introduces… like, this check happens, we check for, like, severity comparison when we check if loggers are enabled.
Which is on the hot bath, even if… logging is, like, disabled for a certain instrumentation. So it's not a huge difference, but it adds, I guess, somewhere in the neighborhood of, like, 300 nanoseconds per call when everything is disabled.
So it seems… it seems also a little bit more ergonomic to use Intum in this case, because you can compare the values directly instead of .value.name.
Which is a little bit clunky.
So… yeah, like, this is… I'm just kind of proposing we change this before stability, and the obvious downside is it's gonna potentially break some people, but we're not stable yet, and this is why we didn't go stable.
And I think, just considering, like, the no-op or disabled path being… important to optimize, it seems… Maybe worth doing this change.
Yeah, Riccardo.
**Riccardo Magliocchetti** 18:04 Questio, like you said, that… We may break some people, like… How do we think this can break?
**Aaron Abbott (Google LLC)** 18:13 Yeah, I think mostly exporters. They would… they would need to not call .value anymore.
**Riccardo Magliocchetti** 18:20 Okay.
**Lukas Hering** 18:22 Or if you had, like, a custom filter.
Something.
**Aaron Abbott (Google LLC)** 18:27 Hallelu no.
**Liudmila Molkova** 18:30 Does it make the enum open, or it will still be closed?
Can someone… It's still… reported question.
**Lukas Hering** 18:40 Oh, sorry.
What were you saying?
**Liudmila Molkova** 18:45 So can I, create a custom severity that's not in the range declared.
**Lukas Hering** 18:55 Is that allowed?
I guess…
**Liudmila Molkova** 18:58 tech?
**Lukas Hering** 18:59 Yeah.
**Liudmila Molkova** 19:00 I was going to check. I think half of the languages make it aloud, half of the languages make it impossible, but I, like, in the long run, if we ever want to expand Well, expanding wouldn't be breaking, right? We can add more stuff.
**Lukas Hering** 19:19 There's already quite a few, I couldn't imagine we'd ever run out.
But…
**Liudmila Molkova** 19:23 Somewhere, like, we can see that there are a custom range defined for something else, because currently, like… It's tied to… This is, like, the criticalness of the error.
But you can say… you can use it in some other custom ways, that… up to users to decide how they use custom ranges.
But anyway, I'll check if spec allows it, but I'm kind of curious if… People think it's useful to have it open.
**Aaron Abbott (Google LLC)** 19:59 My… I think it's not, because I think in OTLP it's defined in… it's like a protobuf enum, not a raw int. I believe protobuf enums are closed by default.
Or they might only be allowed to be closed.
So I'm not sure how we would, like, serialize it if we accept other values, besides falling back to the unknown zero value.
**Leighton** 20:26 Yeah, I'd love to… left a comment on the test and test logs. I think the contributor… Added a case in which you could just pass in an integer. It's the very bottom, whoever is sharing.
Test underscore logs in SDK, I believe?
Oh, the SDK package, yeah.
**Tammy Baylis** 20:54 Sorry, I'm sharing.
**Leighton** 20:56 Yeah, so the very last edited, test.
Yeah, so if you scroll all the way to the bottom, It's like… I left a comment at the bottom of the file, where it's like.
and enum allows direct comparison with ints as well, so I was wondering, it's like.
Is this an example of what you're talking about, Ludmila? Like, allowing flexibility of the API, or…
**Liudmila Molkova** 21:23 Yeah.
And there is no good use case for… For it in this pack, and… I'll check if it's allowed. It's just that, from the API perspective.
it would be more… it would be forward compatible. So somebody, if we ever add more value, somebody who uses the new way and ends up… ends up with the old version of OpenTelemetry API would not Get an exception, but yeah, let's corn our case.
**Lukas Hering** 22:03 I'm actually pretty sure that line would throw a type checker. Like, the only reason that works is by virtue of the fact that this is now an int enum, so int is… It is an int.
I'm not sure if we just have linting and type… well, we don't type check the tests, but the linting might also be disabled.
**Aaron Abbott (Google LLC)** 22:24 Yeah.
**Lukas Hering** 22:24 In my opinion, we probably shouldn't… we should just have the type be strictly… the type hint be… Strictly the logger severity to prevent, like, bugs.
**Leighton** 22:38 Yeah.
**Aaron Abbott (Google LLC)** 22:41 Yeah, I think… I think we could do either way if there's a compelling reason, but… I… I think… what you said makes sense, Lukas, like, this probably doesn't… Probably doesn't pass the type checker, and then it's most likely their implementation also doesn't, It may be interesting to see how it… how it tries to… serialize this in the OTLP tests, if that happens, but… Yep.
**Lukas Hering** 23:13 Okay, I guess, actually, a follow-up to this, then, so, like, I guess, maybe more for Aaron, but, once this is merged, are we comfortable with, merging those log stabilization PRs, or is there anything else?
**Aaron Abbott (Google LLC)** 23:33 No, I think… I think that's pretty much it. I was looking at… Maybe one other… There's some other stuff, but I think it's mostly in the SDK and behind the API. It's like… Right now, we do a lot of boxing in the SDK for the API log record, because the SDK log record implements the API, or it, like, subclasses it.
So there's some strangeness there, but I don't think it's something we can't address later in the SDK.
Cool.
Thank y'all, if… It sounds like we want to follow up on the open vs. closed thing, and then… Besides that, everybody's okay with making this small change.
**Leighton** 24:23 Yep.
**Aaron Abbott (Google LLC)** 24:28 Alright, I think we can move on. Sorry, this was… I'm just merging these together.
**Tammy Baylis** 24:33 Oh, thanks, Aaron.
Yeah, next topic, I believe, it's the… the one that we chatted about briefly in triage? Yeah, fuzz.
Were there any other questions about this one?
**Aaron Abbott (Google LLC)** 24:50 Oh yeah, I was gonna ask, is there, like, a off-the-shelf… suite for this, for, the W3C headers.
**Lukas Hering** 25:05 As far as I could tell, I mean, I need to look again, but I think only the collector does fuzzing.
But… are you, are you saying, like, I guess I'm not sure how… Let me think…
**Aaron Abbott (Google LLC)** 25:22 Yeah, like, some kind of conformance test or something like that for… testing the propagators, just because there's so many implementations. I think… It's totally fine if there's not one. I think this is super valuable to have, our own fuzz tests, but I know some projects, like, they'll do… Fuzzing is a… Like, a test harness or something like that.
**Lukas Hering** 25:47 Oh, okay. Yeah, I'm not sure, like, how you'd actually generalize it, since, like, this uses, The profile-guided fuzzing?
**Aaron Abbott (Google LLC)** 25:57 Oh, I see, I see.
**Lukas Hering** 25:58 with, the… yeah, the Google Lib, which wraps LibFuzz, I think.
Yeah, I guess, like, one question, I don't know if we have the CI capacity, or, like, if we want to maybe, like.
once we build this up more, we could just have it run, like, every Sunday night or something for maybe an hour or so. I haven't looked into it too much. We obviously want to keep, like, the… Corpus that it builds up.
From the profile-guided fuzzing.
And then also, I think we could probably get it integrated with OSS Fuzz, so maybe that's good, too. Good enough.
**Aaron Abbott (Google LLC)** 26:49 Yo.
I mean, I guess it would be… So basically, we choose how long it runs for?
**Lukas Hering** 27:00 Yeah, and then we want… there is some state that it needs to save, just so you're not starting… the profiler isn't starting blind every… or the fuzzer isn't starting blind every time.
**Aaron Abbott (Google LLC)** 27:18 Yeah, I mean, I guess… it's kind of up to you, Lucas, I think.
It's probably just, like, a drop in the bucket if it runs for 30 seconds, I think that's what you had here. Or maybe you had 300 seconds, maybe.
**Lukas Hering** 27:34 I didn't even add it to CI, actually.
**Aaron Abbott (Google LLC)** 27:36 Oh, good.
**Lukas Hering** 27:37 I have this stuff here.
But… Yeah, I was thinking that can be a follow-up.
**Aaron Abbott (Google LLC)** 27:50 Yep.
**Lukas Hering** 27:51 But yeah, probably just, like, a weekly thing, we don't want to, like, use up a ton of CI on this.
**Aaron Abbott (Google LLC)** 28:00 Cool. Thanks for working on this, Lukas. It's,
**Lukas Hering** 28:03 Yeah, if anyone has, like, ideas on what else they want to fuzz, yeah, there's… Yeah, definitely, A lot of areas, like declarative config, we could try fuzzing configs or something. But, yeah.
**Tammy Baylis** 28:33 Alright, thank you. Last topic, Erin, again, POC… POC generating typed monkey patch code across many versions of instrumented library.
**Aaron Abbott (Google LLC)** 28:47 Yeah, so, oh, of course it added that. Yeah, this is a bit of, like, a… proof of concept still, and I tried to make it so that we can see it pretty easy, but… Tammy, if you jump down to patches.eml, Yeah.
So, this is… this is just something I'm playing around with, but the general idea is… to, Generate, like, wrappers.
Instead of doing the raw rap stuff that we're doing right now, Which is a bit… fragile. I think we're seeing this a lot in Gen AI, where we support We're patching internal functions that don't… Have any consistency across versions, so… The general idea is to generate the code, which is that underscore patches.py file, but you can see this is kind of like the input. You specify… The versions you support, number of versions to sample, which is this max policy.
and the, like, APIs that you want to patch here, so this is… Doing it for URLib3, as an example.
And, yeah, if you… so if you go to the underscore patches.py, Tammy… Yeah, so this is… this is what gets generated.
So it's, strongly typed.
Like, wrapper based on, Based on those versions, from, like, actually examining them on PyPy, if you scroll down a bit.
So these… this URL, URL open args is, like, the… Things that the instrumentation has to handle as kind of like, How we have for inspect.bind.
So it's basically giving you the signature, and you don't have to worry about args versus keyword args for stuff. It handles it if there's, like, incompatible ways to pass stuff, and then it handles rebinding.
The arguments the same way they were passed.
And one more thing, you see on line 86, It's showing you that this field was only added after 2.0.2, And it adds this missing sentinel, To… kind of forces the instrumentation code to actually deal with the cases that certain parameters are just assumed to be there in certain versions, versus whether they're actually there in all the versions.
Yeah, and if you go… so there's a bunch of generated code here, it still uses wrapped and all that stuff, and if you go to the init py file.
Yeah, so this is the actual change to, you're all in 3.
So you can see… on 4-19… Yeah, this… this is now, like, instead of the wrapped function, which just passes everything as any, with, like, the args and keyword args, this gives you the typed args bundle And then, like, typed instance and a typed… wrap function.
And, you can see it cleans up some of the code.
A little bit, but most importantly, I think I had… I had, like, some… GenAI agents doing this, obviously, but tried to really focus on it looking clean in the instrumentation code, and… the… I think I found, like, 10 bugs, and I was able to migrate, I think, 20 of the instrumentations to this.
But, yeah, it's still, like, proof of concept, so… I wanted to get people's thoughts, see what you think. Is it valuable?
Yeah.
Lukas.
**Lukas Hering** 32:22 Is that… so that patches .lock file, is that something that we hand generate, or…
**Aaron Abbott (Google LLC)** 32:30 Yeah, so this… This basically is, like, a hermetic artifact, so that the underscore patches.py is generated from a Jinja template, but this is representing the, it's basically the inspect output for each function from all the versions. So this is the… this is, like, the output of looking at all the stuff on PyPi.
And if we update the Jinja templates, you can regenerate the patches.py without touching the internet or anything like that.
**Lukas Hering** 33:00 Oh, okay, so did… so… did you… is there, like, a… like, some side script that generated this? I guess is what.
**Aaron Abbott (Google LLC)** 33:07 Oh, yeah.
Yeah, so, this… this is, like, a PR… draft PR in my… in my, fork. It has two commits, and I tried to just make it easy to… to show here, but if you go to the commit drop-down, there's… I don't know, like a… 1500 lines of code that does all the generation.
**Lukas Hering** 33:33 Got it.
**Aaron Abbott (Google LLC)** 33:37 Yeah, and there's also, it adds, like.
in the OpenTelemetry instrumentation package, it adds some… Like, shared code, yeah.
It had some shared code that it uses for calling Rapt and all that stuff, and handling the Sentinel and stuff.
Yeah, Riccardo?
**Riccardo Magliocchetti** 34:05 Yeah, question.
Maybe you already said, but… Do you do, like, any validation on the version of the… Of the library you're patching, or it's just for reference, but you store all the supported versions?
Thank you.
The, in the patches, there was, like, the list of the… a list of versions for URL3.
These are the lists that are supported, or are the list that the tools are seen?
We're building the… Do you mean, like, does it…
**Aaron Abbott (Google LLC)** 34:46 Do you mean, does it check at runtime if it's… if the signature's compatible?
**Riccardo Magliocchetti** 34:49 Yep.
**Aaron Abbott (Google LLC)** 34:51 Yeah, it checks at runtime. We could also look at the versions.
Installed with, like, an importlib metadata?
And then decide on that, but I should have said before, we had Trask come a couple weeks ago, and he talked about, muzzle and Java, and this is kind of… like, a code gen… interpretation of that. So it's… it's intended to solve the same problem, where it… it gracefully degrades if the… If the installed version doesn't match the signature of the versions we expect.
**Riccardo Magliocchetti** 35:24 Yeah, so, like, it matches the signature, not the version, right?
**Aaron Abbott (Google LLC)** 35:28 Yeah, I think… I think it actually matches the version, but it's open. It might… it might check both, I would have to… have to, dig in a little more, but it definitely allows new versions.
**Riccardo Magliocchetti** 35:37 Because, like I was worrying about every time someone releases something, we need to rebuild this.
I guess not, like, if the signal does not change, the tool should be fine, right?
**Aaron Abbott (Google LLC)** 35:48 Yep, exactly. So it defaults to allow future versions and, And not allow less than the minimum version. And then… The idea is you would just generate… you would update these log files every once in a while, and generate patches to handle new versions if things break.
**Riccardo Magliocchetti** 36:10 Thanks. That's very cool.
**Aaron Abbott (Google LLC)** 36:13 Yeah.
Lukas?
**Lukas Hering** 36:16 Yeah, just another, another follow-up question. So, if a function, I guess, like, how gracefully does this handle, like, if I, like, were to rename an argument or something in a function, like… I'm getting, like, I guess I'm… Yeah. I figure that would be kind of tricky to handle,
**Aaron Abbott (Google LLC)** 36:37 Yeah, yeah, so I believe… And I think I've tested it with… I think some of the Tornado ones, we support, like, 3 versions, and it handles this, but it will add both… both of the parameters.
And then it will give you that missing sentinel value. So, it… assuming we… assuming we have type checking enabled in the actual instrumentation, it should, like, statically force you to… Check that all the fields are there if it's possible for them not to be there.
**Lukas Hering** 37:10 Right, so, like, the new and the old argument would be just, like, optional or something.
**Aaron Abbott (Google LLC)** 37:15 Exactly, yeah. You get… you get two missing variants.
**Lukas Hering** 37:19 Got it, okay, so there's still, like, maybe, like, a teeny amount of work, like… If a new version were to, like… You know, rename an argument or something.
**Aaron Abbott (Google LLC)** 37:31 Yeah, yeah, yeah. So one other thing I played around with was, like.
Generating a different wrapper for the incompatible signatures, so it would do something more like, like, overloading at runtime, where you would… you would implement the right, you would implement a different version for each incompatible signature, and then it would call the correct one at runtime, so you kind of don't have to manually handle that. Is that what you mean, Lukas?
**Lukas Hering** 37:59 Yeah, partially, yeah.
Yeah, this is, this is really cool, though.
**Aaron Abbott (Google LLC)** 38:06 Okay.
Yeah, cool, I, I have, like.
I want to say I migrated about 20 of them, so I think most of the cases should be handled from, like, Contrib.
But, yeah, if you have any comments, please let me know, and I can… Try to… try to extend it to work with different stuff.
Cool, so it sounds like generally people are interested in this, sounds… seems somewhat valuable.
Cool.
Thanks. So maybe I'll polish it up and open a draft PR. People can share feedback, and we can, go from there?
Alright, cool. All yours, Tammy.
**Tammy Baylis** 39:02 Thank you, Erin. One more topic from Dylan, Light LLM.
Yay.
**Dylan Russell** 39:09 I don't know if people saw this, they had, like, another security incident.
And it seems like it has to do with… like, the build and release process during, like, publishing to PyPi?
So, I was just gonna have my agent, like, review the two incidents that they've had, and like… Review our release process and see, like… If we're doing anything, like… Wrong.
I think they… I mean, yeah, they have… a much bigger codebase, and I think they're doing, like… they do, like, crazy numbers of commits.
So… But… Yeah, so there might be reasons they're, like, more vulnerable to this than we are.
**Aaron Abbott (Google LLC)** 40:01 do it.
**Dylan Russell** 40:02 Yeah.
**Aaron Abbott (Google LLC)** 40:03 So I was just gonna ask, at a high level, it sounds like somebody stole their credentials and was able to publish PyPy packages? Is that right?
**Dylan Russell** 40:13 Yeah, some credentials… some, like, OAuth token credentials got… Stolen.
**Aaron Abbott (Google LLC)** 40:23 Yeah.
**Dylan Russell** 40:24 And… They were then able to… Yeah, do a release to PyPi.
Yeah, through, like.
I don't know. I was reading through it, and I didn't, like, completely understand, but yeah.
**Aaron Abbott (Google LLC)** 40:46 Okay, I mean, yeah, that would be helpful if you, if you want to audit it, and let me know if I can help, Help in any way.
**Dylan Russell** 40:55 Okay.
Alright, yeah, sounds good.
**Aaron Abbott (Google LLC)** 41:04 Yeah.
On a somewhat related note, I think everyone remembers, like, our package squatting woes.
There is… let me see if I can find it… there… was a RFC from OFEC who used to… he joined for a while, and I think he was… asking us if this is helpful and all that. So his, PEP was merged for Python.
But I think we're waiting… it's still not implemented in PyFi, I think here's the issue.
This is kind of orthogonal, but I thought I would just share. So, if anybody wants to contribute to PyPi and do this, it would be… Nice to reduce our, like, package squatting,
**Dylan Russell** 41:43 Oh, cool.
**Aaron Abbott (Google LLC)** 41:45 Yeah.
**Tammy Baylis** 42:06 Thank you.
And, yeah, thanks for being proactive, Dylan. Any other topics or random stuff we want to talk about?
Okay, we'll finish early again. Thanks everyone for contributing, and see you next time!
I think it's not.
**Jackson Weber** 42:36 Have a good one now.
**Diego Hurtado (Dash0)** 42:37 Excellent.
