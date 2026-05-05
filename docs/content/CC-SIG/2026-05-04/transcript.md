SIG: OpenTelemetry C/C++ SIG
Date: 2026-05-04
Duration: 69 minutes
Zoom Recording URL: https://zoom.us/rec/share/resksElzep7JtTGN4db7-McbZY2alzo5Iu94hNys5E7CDte0e_2lDYYMTg5q20PB.7oeKHvEDrTyfXZkp
============================================================

## Zoom Recording Transcript

malff 00:02:28 Hi, Luke.
Doug Barker 00:02:36 Hey, Mark, how's it going?
malff 00:02:39 Not too bad.
For some reason, I see two of you on Zoom.
Doug Barker 00:02:45 I signed in from my desktop, and then the speaker didn't work, so now I'm on my phone.
malff 00:02:50 Okay.
Let me show my screen.
Doug Barker 00:02:57 Yeah, hope that that vacation went well.
malff 00:03:00 Yes, it was very nice.
Doug Barker 00:03:15 Alright, I think I might sign in from my desktop again, so you'll see two of me, but one so I can see the screen.
malff 00:04:17 Do you know if, Tom or Lavit are joining today?
Doug Barker 00:04:22 No, no, let me, checked Slack earlier today, and I didn't see any messages.
malff 00:04:27 Okay.
Doug Barker 00:04:29 Tom usually is the only one with me on Wednesday that joins, but then we usually cancel the meeting because nobody else shows up.
malff 00:04:37 Okay.
Doug Barker 00:04:38 I haven't seen Lillette for a little while.
malff 00:04:41 Okay, well, I guess we can start then.
Oh… I saw that you filed a lot of new issues and things like that, and also made some good progress on… Ceiling tidy, and all the… Much cleaner that we have.
So, anything you want to discuss in particular in all that? Why am I looking at this?
Doug Barker 00:05:12 Yeah, I think so. Probably the one would be, especially given the recent, community feedback on the exception handling, so… I have that ticket that's been open for a while that you've commented on.
malff 00:05:27 Yes.
Doug Barker 00:05:28 pull request, and I think… I don't know, my kind of feeling is that probably at this point, we should probably start with creating a, error handling, exception handling policy for the repository.
To maybe give people better guidance?
What do you think?
malff 00:05:45 Oh… Yeah, I think we definitely need to clarify what we should do, because this has been kind of vague and undefined so far.
Doug Barker 00:05:54 Yeah.
malff 00:05:55 So that people are just focusing on, well, the current path, nominal path, but not paying attention to Robustness in our ending, so…
Doug Barker 00:06:09 Yeah, I think that makes sense.
So… I think what I did on this one, it's been a while, I looked at the 3964.
malff 00:06:21 Yes.
Doug Barker 00:06:22 So this one is… are all of the claim tidy, exception escape warnings that were flagged for the API.
And… I think the… probably the remaining question is, is this the pattern that we want? I think I can, narrow the scope of these catches.
further, especially for this one, because we know that this is regex, so I think we can catch the exact exception.
Yes.
malff 00:06:50 If I recall, I think I had a comment somewhere… Yeah, it looks like you, europe, territorially.
some… some of help… things like these, these, which are just helpers, I think it's, Sometimes it makes sense to add no except if it makes… and under the exception internally, like this. Sometimes it makes sense to not do that and do this the other way, like in StrainUTL, I think.
For this stream thing, so… It's a… It's hard to find the right, Right place, 200 exception in that code, because it's, What we know is that externally, an API call needs to be no exception, but then, internally, there are so many helpers in left and right.
But, maybe not all developers need to… To be flagged, no accept, so we need to look in details.
Doug Barker 00:07:59 What's your gut feeling on this? Like, you know, should we be trying to put the try-catch as low as possible around the methods that we know we'll throw?
As opposed to… making these, helper methods no accept, and then doing high, higher level try-catch at the no accept API method.
malff 00:08:18 Yeah, it has been a long time since I saw that code as well, so no strong opinions there.
whatever seems the most natural, I guess.
But in case… for the specific case of all the regex code, I think the regular expression code should be… Should have a try-catch so it doesn't propagate all over the place.
Doug Barker 00:08:44 Yeah, I… That's kind of my gut feel, too, is to do the try-catch at the lowest level, like, right around the methods I throw, and then see if we can make the call chain no accept going up to the API. Does that sound like the right approach?
malff 00:08:59 Yeah. Yeah, he does.
And another thing I think I mentioned as well, All the code under plugin, it's… it's not used, so… And it's flat for removal, so… If we want to fix it, just to pass the scene ID, fine. Otherwise, we can just also add suppressed comments just to not deal with that, and not change the… change the code under a plugin detail, because we… it's dead code, so it's… there's no… my point is, there's no point fixing it, because it's going away, very soon.
Doug Barker 00:09:44 Okay, fair enough.
I think I might have reverted that in this one, but maybe not. Maybe it's just this, changing this OpenTelemetry have exceptions, because I think that that is a legitimate thing that needs to happen. We shouldn't be using the… Underscore, underscore, exceptions.
malff 00:09:59 over, yeah, this thing, yes, definitely this is legitimate.
Doug Barker 00:10:04 Yeah.
malff 00:10:07 Yeah, things like that, yes.
Okay, I'm back from vacation, so I will take a look again at that PR and provide comments.
So that we can, make some progress on it.
Doug Barker 00:10:22 Okay, and I'm… I'm not in a rush to merge this. I think what we could do is we could draft and have an issue in PR to draft, like, the policy first, and maybe we use this one as an example or something, but then that would allow everybody to have better guidance as we try to fix all of the exception escape warnings.
malff 00:10:41 Yeah, yeah, sure.
looking at all the cleanup that was done for sale and tidy, I was hoping to get to zero, but even if we don't get to zero for Israelis, it's not a big deal, because CI… no matter what we do, CI has a way to enforce that we have less and less warnings anyway.
So, if we have a few which are unresolved, it's, nothing to worry about, anyway.
Doug Barker 00:11:09 I mean, we could get to zero. I think it's just having that policy so that everybody knows what the strategy is, you know?
malff 00:11:15 Yes, yes.
Doug Barker 00:11:16 catching the exceptions, because it's not terribly difficult once we, I think that, you know, the harder ones have been done, which require a little bit more minor refactoring, but for catching the exceptions, I don't think it'll be too terrible.
malff 00:11:29 Yeah. Yeah, once we have clarity, it should be easy to apply.
Okay Just so you know, also, where is it?
Oh, this thing with Rapid YAML.
Doug Barker 00:11:51 Yeah.
malff 00:11:52 As you noticed, there is a code change.
well, a breaking change in epidemic itself, so I need to see… how to… there wouldn't be a code change to use the proper API for error handling, and most likely this will… This will depend on the exact lampedermal version to use, so I need to investigate this and fix it.
So, it's.
Doug Barker 00:12:24 I think that's fine. We'll just need to communicate on this one, and I think since Rapid YAML's not yet to version 1.0, so we'll expect some breaking changes, but we'll just have to make sure to communicate in the release notes that the minimum version also changes for Rapid YAML, so there's only one version supported.
malff 00:12:42 Yeah. Well, we… We don't need to. We have… we can still support multiple versions. I think we do already, because we don't… In CMake, you had the minimum and the maximum requirements for third parties.
And I think we are using… we are supporting two different versions right now, if I… if I remember correctly.
Doug Barker 00:13:09 Yeah, but I think with this change, it's gonna be a change to our code to fix this, I'm guessing, with these callbacks, so then it would no longer support the older version, unless you, handle it somehow, I don't know if that's worth it.
malff 00:13:22 Okay, well… I will take a look to see what the change is exactly anyway, and then we can… we can figure this out and decide.
Okay. But there is a way to have code that depends on the rapid YAML version.
So it's, it's possible to do that if we need to.
Doug Barker 00:13:42 Okay.
malff 00:13:51 Yes, another thing, so, as you have seen, I don't know if you noticed, but there was a huge discussion in community a while ago.
We have a new process to basically look at, every, member, like, approver, maintainer, and whatnot.
To see if there's any activity, and if not, PRs are now automatically filed by workflow, like this thing.
So, this is… This is a PR to just make some cleanup for Josh and, And I forgot his name.
And Panav, yes. For approvers, there is also the… there is also a similar one in CPP Contrib.
Doug Barker 00:14:47 Yeah, I saw that one.
malff 00:14:49 Okay. So, interestingly, in CPP Contrib, so… Typically, one repo has one list of maintainers, so that way, the repo and the list of maintainers is in sync.
However, for C++, there is one list of maintainers, and we have many different repositories, so CPP is the obvious one, but there is also CPP Contrib, CPP BuildTools, and I think that's it.
And in case of CPP contribute, so you, you are a maintainer there, by… By being a maintainer of OpenTelemetry CPP, you automatically are a maintainer of CPP Contrib.
But the script itself does not know about that, because it's only looking at the activity in this CPP control repo.
Which is why… why is this thing?
So, which is why I tried to kick you out. So, I think the one thing that we should do is just to add you in the README as a maintainer, and if you had time to do that, I think you should do it, because then that will count as a PR with your name, so the script will see activity from you, and will not try to kick you again next time.
Doug Barker 00:16:14 Okay.
I can do that.
malff 00:16:21 So, it's just a matter of, Adding your name in worried me.
You have all the rights already, so all the administrative part is done, so… should be… Yeah, it's just a matter of running one line like this.
And for… for both, for, CPP and CPP Contrib, so this is… this is brand new, because this workflow Yeah, so this is the new workflow that was designed for that.
This is the first time this workflow is actually used.
So, over reports, have the same kind of PRs, and… The consensus is to just wait for a full week, to get any feedback from, The people concerned with that, to see, if there are comments.
So… Please don't merge that right away, we need at least to wait one week to decide what to do.
And I think, yeah, I think I added a comment.
Yeah, format.
Doug Barker 00:17:32 So who's gonna be left on OpenTelemetry, contrib?
After this one.
malff 00:17:39 So, telemetry contrib, once… I can, I can address the PR to remove, to… Either not remove your name, or… once you are added… once you write the PR to add yourself to maintainers, I would adjust the PR to… To account for that.
Yeah, so this is what we just discussed, just… please, please add yourself as a maintainer in CPP from Trip.
interview.
Doug Barker 00:18:24 Yep.
malff 00:18:27 The main thing I wanted to discuss, but also with Lalit, because he has been following that, Are you aware of, well… Let me see… Okay, so this thing?
It's all public now, but this started as a security report against the Go repository, complaining that Typically, when we send a… we do an HTTP post against an endpoint.
To send the… send the data, and the endpoint can reply with a message.
And we try to read all the message in memory without questions. So, if you happen to talk to a server which has been compromised somehow.
The server can force you to Allocate a lot of memory, and then, you… you end up with… With a large memory conception, yourself.
So, that was… This is public now, this is… The probability of this to happen is extremely low, because you need to knowingly… well, you need to somehow talk to a compromised server.
So the likelihood of this, happening is low, and… There are other things that need to happen before that, but still, it's flagged as a security issue, so we should fix it.
And I went, so… all that is public in other repos, and I was wondering the way to fix it, we can either fix it as just a regular PR, because everything is public anyway.
Or we can try to follow the proper process, which is, in GitHub, there is a way to report a security issue, which is private, then there is a way to… fix that PR in a private branch, and have the code review on that private branch.
To… to make the fix work, and then only then the fix is merged to the main code.
I wanted to have your opinion whether we should actually try to use the tooling to follow the process, or we should just fix this as a regular PR.
Doug Barker 00:20:58 Do you know what the other, SIGs are doing with their approach is?
malff 00:21:02 Well, the… I think others did that in a private PR. Well, actually, it depends on which… many repos are affected, so Java… I'm not sure if everyone did this the same way.
Huh.
The issue is public now anyway, so there's no point in hiding the fix, because if you look at… in other repo, you see exactly what the problem is and how it was fixed. I'm asking just as a way to train ourselves to use this, this private branch thing, so that Next time when we have a really issue that really needs to be private, so at least that we have… we are familiar with the tooling and the process.
Doug Barker 00:21:46 Yeah, I'd be open to it. I think it'd just be good to understand what the process is.
malff 00:21:52 Yes.
Doug Barker 00:21:53 seen that before.
malff 00:21:54 Okay, so I'll try to do that. So, what I will do, I will file, file an issue, try to create a private branch, and I will ping you on Slack with the details to make sure you can actually see that, and… So that we can… we can do the fix and the code review on that.
See, see, basically, if he, if, if it… If we can all see the PR and work together on it.
Doug Barker 00:22:27 Perfect.
malff 00:22:45 Actually, I've been away for 2 weeks, so, I guess it's, can you tell me… If anything special happened that needs special attention, As I'm not aware of.
Doug Barker 00:23:00 I think the security one is probably the top priority, so I think you're right on that one. And then, regarding PRs, I think we've, you know, I've been logging kind of like a mix of some really easy, super easy issues, and that has pulled some new contributors in, which is interesting.
malff 00:23:17 Yep.
Doug Barker 00:23:18 Then, we do have some PRs that have been around for a while. I think, Owens, PRs, you know, have been there.
That one, yeah.
So I think that one's getting close. I'd like to get that one in, and then… I have a, Do Not Merge PR that I'm waiting for this one from Owen to get in, and then I'm going to clean up the, the no SDD variant access, hopefully get a little bit of a performance improvement and fix some additional warnings, but that's dependent on getting Owens in.
malff 00:23:53 Okay.
Yeah, from… this one, for a moment, had a… I had a comment earlier asking for, basically, a CMake flag, and he implemented that, so, I'm happy with that PR itself. The only thing I found is let's see… Yeah, there is… so there is one place where I need to set the flag, use that compile time, but this is just a minor change there. And otherwise, I think this PR is ready to go.
Doug Barker 00:24:35 Perfect.
malff 00:24:46 So, yeah. One thing I will do, a new version of semantic conventions was released two weeks ago, or last week, I don't remember.
So, as usual, I will just generate semantic conventions again, so you should see a PR for that very soon.
Also, I saw that you and Alit had a discussion on this thing, on span limits.
Doug Barker 00:25:39 Yeah, I think this one, in my mind, is kind of bringing up a larger architectural issue, and it's kind of being exposed by the push for the configuration.
malff 00:25:50 Yes.
Doug Barker 00:25:51 schema, and the architectural issue is really around, I think, this recordable idea.
malff 00:25:57 Yeah.
Doug Barker 00:25:58 And, you know, I, I think this probably needs to be addressed in some way, but the way that the span limits were implemented, you know, it's a little awkward, and it doesn't really match the model of the spec now with configuration, so there's kind of a.
malff 00:26:15 That's impressive.
Yes, so, yeah, so the… the spec and the YAML part, especially just… Put the same limits for everything.
Doug Barker 00:26:26 Yeah.
malff 00:26:26 Because the limits are attached to the… to the processor, I think, I don't remember, so you don't even know which exporter is used when you specify the limits.
Doug Barker 00:26:37 Right.
malff 00:26:38 And so, yeah, so there's… The way to specify that is at the top level.
the thing, so, in the spec, the specs also says that, yeah, the SDK should enforce this and do that on the limits and so forth.
And I think that, There are two ways to… to read that statement in the specs. So, one way is to say, well, the spec says the SDK should do this, so… We should have an SDK class that actually does that, which is one way to read that.
And the other way is to say, well, the SDK as a whole should enforce limits, and how it does it, whether it does it by itself, or if it delegates to the exporter to actually do the job, is up to implementation details.
And I think this is where the… the discussion with Reddit is coming from, I think he's, so he's right that we don't want anything in the odd path to make the code slower.
But I don't think we need to, if we… If we can somehow reuse the logic that we have today in the exporter and enforce limits.
It's just a matter of passing the parameters there.
All the way down, from the… From the configuration.
Doug Barker 00:28:04 Yeah, I was reading… So I think… I think that, if you… if you go back, you know, I was following the discussion from Lillette and the contributors for this particular feature, and I think there's a disconnect in Lillette's, you know, guidance and understanding, of how the feature was actually implemented, so… you know, the like calls out that it wasn't, supposed to be in the hot path, you know, on these methods like setAttribute, addLink, addEvent, but that's how it was implemented. It's just now… Per… exporter, so we only have it working on two exporters now, so it's only on the OTL… OTLP HTTP and OTLP.
malff 00:28:47 Obviously.
Doug Barker 00:28:48 But it is in the hot path, so we're paying for it, we just don't have, you know, now we have that configuration set.
And it may be, you know, it also add… adds more data to each… each and every span, so they now all have the max limits, those constants, like, is data that is carried along with every span now, you know? So I think… if we're going to do that, then I think my argument is, like, we probably should just put it in the SDK span, so then all the exporters get it, and then we can configure it as, I think, the spec intended. Yes. If that makes sense.
malff 00:29:30 Yeah.
Doug Barker 00:29:37 But I think… I think the core issue, that LED's probably pushing for is, like, the recordable idea doesn't have accessors, so there's no way to get how many attributes, or how many events, or how many links have been currently added, you know, and that's…
malff 00:29:54 Yeah.
Doug Barker 00:29:55 One of the… also one of the challenges that'll… that is gonna block us from directly addressing, a lot of the spec requirements around processors and samplers and… and, other things that can be configured, you know, either through YAML or.
malff 00:30:11 Yeah.
Doug Barker 00:30:12 API.
malff 00:30:14 Yeah, and… well, especially if there are things that, we can have some samplers that add attributes by themselves, for example. Right.
depending on where we… just counting attributes, I mean… If we count them on the recordable at the end, or if we count them in the span when we see add attribute.
We may be counting something different, so it's… We need to clarify where to put all that, yes.
Doug Barker 00:30:49 Yeah. If we… if we hadn't…
malff 00:30:50 Yeah, if we… if we end up doing… having that in, in the exporter.
The other thing is… so, we most likely have more efficient code.
But the other thing is, this will be only working for OTLP HTTP and OTLP gRPC, and not for the other exporters, so… Maybe it's okay, but at least we should… document that clearly is saying, well, this feature only works for that exporter and not everything, which is a bit surprising, because the configuration is totally, Ignorant of where it goes.
Doug Barker 00:31:26 Right. Yeah, and that's my argument. I think it just… it's gonna complicate the architecture a little bit to add all these accessors now to set span limits, and then store them on each and every exporter, and then you don't know if the exporter actually implemented it, you know, correctly.
malff 00:31:42 No.
Doug Barker 00:31:43 So I… And we're already paying for it at the… in the hot path, with the two exporters that everybody's using, likely the OTLP,
malff 00:31:54 No.
Doug Barker 00:31:55 ones, so… My proposal to move forward, and it kind of ties into my next topic, is on benchmarking, because right now we don't have a benchmark for the OTLP hot path, you know.
malff 00:32:06 Boom.
Yes, and… Yeah, and this is the other side of that discussion also. It's… so far, it's discussion on reading text. It's no discussion, even reading code, and even less the benchmark results, so… It's… there's a lot of fear and speculation as well.
Doug Barker 00:32:26 Right.
So that was my thought, is, like, right, to ground the discussion, is I can put up a PR to add, some of the missing benchmarks, and I'm thinking of, two primary benchmarks. One is on, like, the record path, so this would be our hot path, so when you're creating the spans and adding attributes and events and links.
And then test, you know, kind of like a nominal case, and then test, like, the max case, if you add the maximum, you know, number of attributes and links and events.
malff 00:33:00 Hmm.
Doug Barker 00:33:01 And then, the other one would be on the export path.
You know, testing, converting that to the… to the full protobuf message.
And seeing that.
I don't know.
Looking at a lot of the discussions around the recordable idea and, like, how its performance is being understood.
It seems like… it was… it was originally benchmarked as kind of a record and export as one thing, and I wonder how you guys have been thinking about what really matters. Is it really the record path? So just creating the span and adding the data to it?
Versus the actual, you know, export and serialization.
malff 00:33:45 I think the… the primary goal there was to… To not create, intermediate structures with all the data, but just create the final message, alone.
So, whenever a span is created and attributes are added and so forth, it just creates the final portal buff message.
Oh… well, step by step, but it's only the… it's the polygraph message which is… which is created, so that by the time the export and needs to send it, it's available and there already. There is no need to… Translate an internal structure with a list and a hash map of attributes and whatnot into yet another format just to export it.
So the primary goal was to just create the final data structure the proper way.
And it's… it's kind of a sinkhole, so the data goes in, but there's… there is the concept of a read-write log record, I think, where you can… not only… so far, we're only writing data to prepare it before exporting it.
But there is also a concept of a log record that you can read back to inspect it and change things eventually. I think this may be… well… Samplers might need that at some point, I don't know, because there are some intermediate transformations, also, which are possible on another record, but we are… we're not doing that, I think.
So, the… The main discussion… the main design so far was to just Only right to the log record, never inspected bug.
If we could, can avoid it, and, Just write the data only if it's going to be needed to export it after that.
Doug Barker 00:35:42 Yeah.
malff 00:35:43 Mostly the concern is efficiency.
Doug Barker 00:35:49 That makes sense. So maybe… maybe the benchmarks are probably the most important thing right now.
malff 00:35:55 So the…
Doug Barker 00:35:56 Have those, we can start to look at the re… the… the real, real, results, and… and have a discussion, what to do. Yes.
malff 00:36:05 Yeah, and I would say that regardless of the discussion, even regardless whether we implement limits or not.
benchmark will be important, because I'm sure there's a lot of optimization that we need to do to To improve things in general.
Also, and benchmark will be a way to… to measure that and decide, okay, is that code better or worse compared to this code? And have a final answer on that.
Another thing also that, from this discussion, Lalit mentioned that, yes, this feature is optional.
So, we don't really need to implement it.
I think we still need… will need to implement it at some point, and I think there is also a security aspect to it.
we just saw with HTTP, like, okay, if the server is returning you some insane amount of data, you should not use it all and not die, By becoming out of memory.
Well, the same way… if an application is using a library, and that library is instrumented by adding thousands and thousands of attributes in the span, maybe we should be robust against that. So, if a library is somehow poorly instrumented and generates a lot of things.
If we… if we don't limit the number of attributes, or the number of links, or the number of whatever.
We will also end up consuming a lot of memory, and potentially.
Either die in the… well, either the application will die, or maybe we will kill the… the endpoint would… when that data would be sent to the endpoint as well. So… for robustness, I think we should implement those features, even though they're flagged as optional.
Doug Barker 00:38:05 Yeah, I agree. I think it's important. I think there's a lot of other limits that aren't optional.
I don't remember if there's limits on baggage, but I believe there's other, like, attribute limits and cardinality limits that…
malff 00:38:18 Oh, oh, yeah, I'm sure there are a lot of them, like the size of an attribute, the number of attributes, the length of a value, I mean…
Doug Barker 00:38:25 Yeah.
Yeah, I think it's important. I think, like I said, the main thing that, for me, this brings up is, like, the… the… configuration is starting to make it really well-defined how users are supposed to interact with the architecture, and that's exposing some of the limitations, you know, of the architecture now. We'll just have to hopefully look at benchmarks and then figure out how to address it.
malff 00:38:52 Who knows?
Yeah, and I'm actually quite surprised that this is a side effect of all the YAML projects.
Because… Earlier, I mean, earlier we had, like, a bunch of specs all over the place, and some code, and sometimes we say, oh, there's a new spec, we need to implement it.
But it's… with the noise, with everything changing all the time, it's very hard to keep track of, are all the features implemented? Did we miss a new requirement somewhere? Did we miss a new spec PR that changed something we should be aware of?
And even with that, That, traceability matrix, which is supposed to keep track of what was… what is done, what is missing.
Well, first of all, the matrix is not even up to date, and… and even then, there are parts where we just However, there is no entry in the matrix, so things are forgotten, because.
Doug Barker 00:39:48 You're…
malff 00:39:49 Come back to the spec and read it again.
Or if they are in the matrix, maybe they were overlooked at some point, and never changed, and maybe they need to be revised, and things like that.
But with the Yammer side, I mean.
at some point, every construct in YAML needs to land somewhere, and this thing was actually pretty good at finding all the rules that we are missing.
Doug Barker 00:40:14 Yeah.
It's a good point. I was kind of looking at some of the issues that you logged. Do we have one spot or one, maybe, tag in GitHub for all of the YAML-specific issues that need to be addressed?
malff 00:40:29 We don't have a tag, we have, very something.
So, for all the YAML thing, there is also… A file that defines which feature is or isn't implemented per each language.
So, in that case, for CPP, There is this HTML file that says what is supported.
So… Aggregation, we support samples, we support blah blah blah, and when there are some things that are not supported.
For example, because they are experimental, or they are not supported because they don't make sense, but basically.
This is, we… some sort of, traceability matrix, language by language, for all the nodes that exist in YAMBL with… with a node type. So there is a node of that type, and in C++, We… it doesn't apply, so it's not implemented.
Now, if you go back there, this is the list of all the… all the nodes that we are not supporting currently.
So, there is… basically, this is the gap of what C++ is not doing compared to the YAML spec.
Doug Barker 00:42:09 And then, like we talked about, there's probably some here that are being read into YAML, but are not fully connected. Like, the span limits, I don't think, is in here.
malff 00:42:17 Yes, so some of them are parsed and are represented in memory, but are not used at runtime. And for those, there should be some comments with a fixMe in the YAML code itself.
And I think in that case, well, there's a comment in the code saying this… basically, this is not used, and at runtime, if we ever try to use it, we should see a warning complaining that, hey, yes, I detected this setting, but I'm not doing anything with it.
Things like that. Let me try to show you an example.
Doug Barker 00:43:05 Yeah, I was just thinking, one thing that we could do is, log an issue for each of the Specific items that's… that's missing, with a little bit.
malff 00:43:14 Good morning.
Doug Barker 00:43:15 Well, and maybe that would, drive some contributors to, yeah.
Yeah. Okay.
malff 00:43:20 So, yeah… Typically, this is a comment saying, well, there's a… there's something in the YAML file that we passed, but we're not doing anything with it, and… and this is because of issue so-and-so that needs to be implemented.
Can you, can you see the screen?
Doug Barker 00:43:39 Yes.
malff 00:43:40 Okay, yeah.
Doug Barker 00:43:46 Hey, Tom.
malff 00:43:48 I don't.
Tom Tan 00:43:49 Hi, apologize for being late.
Doug Barker 00:43:56 doors.
malff 00:44:01 Well, that's okay, we just decided that, every open… every remaining bug would be assigned to you, so… Yeah, so, well, basically, Duke and I were discussing a couple of, issues and PRs, but, overall, the main thing is, Oh.
Well, of course, there are some PRs to look at. One thing which is… which is some, Clarification is all the exception ending, to define exactly how to, Auto-do exception ending in the code with a no exception, with no except.
Closes.
So… We'll be looking at that.
Another thing is, as you noticed, there is a new workflow that moves people to MIT status.
So, let's see… Like this one?
So, I'm just waiting for a week to… To see if anyone has a comment on that.
And there is the same one also in CPVontrib.
And the main thing I want to discuss also with you, Tom, is, for security issues.
So, we do have some, some security reports, related to how HTTP Should not read blindly the reply from… the response from a server, so we need to address that.
I was wondering if the best way is to just file a bug as usual. Well, I mean, post a PR as usual and comment on it, because everything is public anyway, so there's no, nothing sensitive.
Or if we should still try to… to handle that PR as a security bug, namely, to create a… Create a security report for that and attach it to a private branch. The point being just to be familiar with the tooling.
So that when we… when we fix the issue.
It's no longer sensitive because it's public, but at least we are familiar with the tooling, so that the next time we have to deal with something.
Who will be better prepared.
So I don't know if you have any, Any preference or comments on that?
Tom Tan 00:46:58 I don't have, I think, even… I haven't seen… And an issue, or… I'm not sure I remember, some issue is reported this week to the… Security… tab. So… so I think it depends, like, for a severe issue, maybe we should still go through the security report process, but for general one, maybe acceptable just to, like, to issue NPR publicly.
malff 00:47:31 Well, so, there is one which is public, which is, Which is this one.
So, yeah, typically this is how a security report looks like. This one is public from Go, so it was…
Tom Tan 00:47:55 So if the source is public, I think…
malff 00:47:58 So…
Tom Tan 00:47:58 be.
malff 00:47:59 It's published, so yeah, it has all the details there. I'm not going… I'm going there, but so, yeah.
So we should do… we can do something like this, to end up the HTTP issue.
And also.
There is another one which was discussed in Slack, which is potentially touching the baggage propagation.
So, but when… I don't… I have not looked so much so far at all the details, but I think this one is private, so we should Most likely ended privately.
Tom Tan 00:48:35 Okay.
Okay, if it comes private, I think keep it private makes sense.
malff 00:48:42 Yes.
Tom Tan 00:48:43 then how should we address that? We still need to send a PRR.
I am… to the public.
So…
malff 00:48:54 from… I've never done that, but… and I'm not going to all the screens because it's… this call is recorded, but from my… in my understanding.
Where we can add an advisory?
And which basically, creates, something similar to that. And then, on the advisory, I've not tried yet, but I think from there we can create a private branch to… for the PR itself.
So, the private branch, then, we can… Maintainers should be able to see it, to see the code, post to it, comment and whatnot.
And then we'll have a private branch to look at that.
Tom Tan 00:49:41 Okay, so once, like, a review passed, and then it will move back to the public?
Man, alright.
malff 00:49:48 Yeah, yes, once it's approved, by the time it's merged, the issue becomes public, I think.
Tom Tan 00:49:58 Okay.
Maybe we can… For all of such changes before release, which would reduce the… the duration… Which is, the issue is exposed, but no new release to address it.
malff 00:50:15 Yes, yes.
Yeah, so basically, prepare for release and merge that at, at the end.
Tom Tan 00:50:22 Yeah.
malff 00:50:24 Okay, okay, what kind of bet.
Tom Tan 00:50:27 Yeah, I think this issue is… this process is good, like, for severe security issues.
malff 00:50:33 Yes.
So, the other thing, it doesn't sound that severe, and this one, I don't think it is severe, but yeah, at least I would like to… See how this process works, so that we are familiar with it.
Tom Tan 00:50:44 Okay, yeah, I think, yeah, that's a good idea.
malff 00:50:49 Okay, I will prepare for that.
Tom Tan 00:50:52 Thanks.
malff 00:51:00 And yeah, apart from that, nothing… nothing new for me. So as you know, I'm back from vacation. I was not there the last two weeks.
Tom Tan 00:51:08 Okay.
We'll come back. So your new release was discussed, right?
1… dot, dot 27.
malff 00:51:19 Yes.
Tom Tan 00:51:21 Okay. I think before, I have a potential PR, but I think that PR is not blocking, so it's fine to not include that. I think the PR has not been raised.
On the ETW exporter.
malff 00:51:37 Okay, well, if you have… if you have a PR, just, comment…
Tom Tan 00:51:45 Yeah, okay.
malff 00:51:46 If you have a PR event you want to include, just comment it, so that we'll add it to the list.
Tom Tan 00:51:51 Okay, sure, yeah, sounds great.
malff 00:51:54 And yes, as we discussed also, there is the fix from Ovent, that I think is ready, so we need to… To make sure to include it as well.
Tom Tan 00:52:02 Okay.
malff 00:52:04 the UTF-8 thing.
Tom Tan 00:52:08 Okay.
So, we plan to… Release a new… to the new release this week, or expectation?
malff 00:52:21 Yes. I'm not sure when I will do it, because there's a holiday coming this week, but…
Tom Tan 00:52:28 Very sweet.
So there were some ABI breaking changes.
malff 00:52:33 Oh, yes. It will not be included.
Yeah, this is something I started to check.
Forgot about this one, so… Yeah.
Tom Tan 00:52:45 Logger.enabled.
malff 00:52:48 Yes.
Actually, I created the discuss tag just for that, so… should… should use it once in a while. Yeah, so this… sorry. So this issue… This fix, is touching Logger, and it's touching Logger in the API.
And it is… Creating… A new virtual.
Tom Tan 00:53:15 New virtual.
malff 00:53:17 I haven't seen the recent messages yet.
Tom Tan 00:53:21 I need to reply.
malff 00:53:23 He replied, okay, so yeah, the fix is probably to use that.
So that we only change the API in the version 2.
Okay, so… I'll look at the details of that discussion, but yes, the… Most likely, we will be… Implementing that change, well… the new method only in API version 2, and actually this was… and this was taken care of, because this is a new commit.
Yeah. When I look at the code, this line did not exist yet, so… Looks like it's taken care of. Okay.
Okay, great.
Okay, this is it for me, I don't have any other things you have… Endotropic Or do…
Tom Tan 00:54:29 No problem, I said.
Doug Barker 00:54:32 I just had the, we talked about the exception error handling, so I'll log in an issue to, start to draft a document that we can put in for, like, a policy on that.
malff 00:54:42 Okay.
Doug Barker 00:54:43 on the benchmarking, I had noticed a LinkedIn issue below in the previous notes about There appears to be a bare metal runner that we can request access to, and I was just curious if you guys thought that was a good idea, or had done that before, or what's your thoughts?
R.
malff 00:55:02 I've never used that before, so I don't know how it works.
So, one thing for sure is that all the benchmarks which are, reported today, the only thing they are measuring is the temperature of the server when they are executed, so… They are not measuring the code, they are just so random that it's barely usable, if at all.
So, my guess with a bare metal runner dedicated for that, at least we would have some more reproducible results.
Which means, if we have valid data in the benchmark, at least we can make the correct decisions.
That would be better. As far as how to ask for it, I have no idea.
Doug Barker 00:55:52 It's in that… so there's a, a Slack channel for, I think it's hotel benchmarking, and then this issue was an example from, I think, the Rust SIG requesting access, so…
malff 00:56:03 Okay.
Doug Barker 00:56:04 if, If that looks reasonable, I can look at that process and follow it, if you guys think that's a good thing to do.
malff 00:56:13 Yes, I think so.
Doug Barker 00:56:14 Okay.
Tom Tan 00:56:15 Yep.
Doug Barker 00:56:19 Sometime.
malff 00:56:20 I'm sure for… so for these things, I'm sure there's a… There is most likely a matter of costs.
I have no idea if the CNCF is covering that, or who is paying for that, but… I'm assuming that if we're allowed to use that, well, we might as well do that.
Doug Barker 00:56:43 Okay, that's an interesting thing. Yeah, if there's any information that you guys have as maintainers that we should be looking out for as far as cost, let me know, too, because there's, certainly things we can do to improve the efficiency of our CI runners, for example.
malff 00:56:57 Oh, yeah, we should. We should.
Doug Barker 00:57:00 Probably our biggest cost.
malff 00:57:03 Yeah, well… There are limits anywhere we try and frost, so… If something is going totally crazy, we will notice, because some of our jobs will be killed at one point.
So in the meantime, yes, we should, also evaluate CI and make sure that it's more efficient. This is yet another big topic.
Doug Barker 00:57:26 Yep.
Perfect.
malff 00:57:28 It's not only, well, the amount of CPU used, but also the time it takes. I mean, sometimes when we have a couple of things to merge.
Oh… because we enforce that every… every PR needs to be up-to-date with a main branch, It generates a lot of merges, each time with the most recent code.
And the time it takes to do a full round of CI is, like, 2 hours, maybe, or at least 90 minutes.
So, if you need to do that 5 times, because 5PR just got burst.
Then you spend a day just, getting the final pill to build and be ready, so it's… Yeah, it's… it's taking some time, so…
Doug Barker 00:58:22 Yeah, we're definitely building a lot of GRPC over and over.
malff 00:58:25 Yes, yeah, that too.
Oh, by the way, I saw a PR to use CLANTIDE in a Docker environment.
For development, and… No.
Where is this… This one… Oh.
So, looks like a good idea, because so far, we've included what you used, and… The only way to know what's going on is to file a PR, do a commit, wait for GitHub to pick it up, and see if it complains somewhere, then try to fix it and try again.
Which is very inefficient, and also takes a long time.
Because the feedback loop is very long, all that to just change one out of file and start again. So… If we have a way to do that locally, using a dev container, that would be much easier for us, first of all, but also for contributors trying to work locally on their PR.
So, I don't know.
Doug Barker 00:59:39 I haven't looked at this, did they, did they… it looks like they bumped… include, use the… to use, version 20.
LLVM place.
malff 00:59:51 I think so.
Doug Barker 00:59:52 Okay.
Tom Tan 00:59:53 Same question, some new… new one is introduced.
Doug Barker 00:59:58 Yeah, and that's the challenge, is like, anytime we change LLVM, which changes the include what you use version, or the C++ version, then the include what you use catches and… or has different strategies, I guess, for finding the warnings, so then we get all new warnings and change all the header files again.
malff 01:00:15 Yeah, it's not that stable, I would say.
But, I mean, at least so far, it's, So, I remember it was very painful to get all the editors correct, at least correct according to one version of Include what you use.
And then, of course, when the version of Include what you use itself changes, there are some adjustments to make.
Because of bugs in Include Reuse itself, or things like that, or… So it's… it's not as deterministic as I was hoping it to be, but it's doing a decent job to… To find things, so…
Doug Barker 01:01:02 Yeah, maybe it's worth talking about this, because I also logged and issued a bump to LLVM22, and maybe if we're going to change all the header files again, maybe we just go to the… the latest version that includes UU supports. That's going to bring new claim tidy warnings as well, but I think we want to fix them.
malff 01:01:20 Yes, yes.
Doug Barker 01:01:26 Bill Okay, I'll take a look at this. I assume that the… The contributor added, like, a new warning limit now to include what you use.
with this change.
malff 01:01:39 I don't know, I've not looked in details.
But at least, yeah, it's… This makes it more… this makes it easier to actually do a run with include what you used to see for results locally.
Which was… Not so easy or, not so easy before.
So, yeah, if you'll… if you have time to take a look.
Doug Barker 01:02:16 Okay. Yeah, I think… I think the only question would be is, like, how do you feel about changing all the header files again? Because that probably is gonna bring up some number of warnings, I don't know how many, but…
malff 01:02:26 Yeah.
Doug Barker 01:02:31 Alright, I'll take a look.
malff 01:02:32 Yeah.
Well, if… I mean, depending on the change reported, if there is a factual reason to say, hey, this error is missing because of such and such reason, then it's something we need to fix.
I don't think the… The headers will be so different between two versions of the input that you use, but we never know.
Like, if somehow it figures out that, yeah, this thing absolutely needs to be included, or this thing does not need to be included, and a forward declaration is enough, we can have change like this, but maybe But, well, I guess we'll see when this happens to… and evaluate them.
Doug Barker 01:03:19 Yep.
malff 01:03:29 Okay, well… It's getting late here, so I think we can, Close the call unless we have other things to discuss.
Doug Barker 01:03:40 Sounds good.
Tom Tan 01:03:41 Thank you.
Don't…
malff 01:03:44 Okay.
And thanks all for attending, and see you soon online.
Cheers.
Doug Barker 01:03:51 Because…
Tom Tan 01:03:52 Bye.
malff 01:03:54 Yeah, bye.
