SIG: OpenTelemetry C/C++ SIG
Date: 2025-11-03
Duration: 78 minutes
============================================================

## Zoom Recording Transcript

Tom Tan 00:00:48 Hey, Hassan, good evening.
Hi, Mark.
Good evening.
Marc Alff [MySQL] 00:01:15 Hi, Tom. Good evening. Good morning, sorry.
Oh, good afternoon, Agnes. I don't always remember.
Tom Tan 00:01:25 Yeah, yeah.
Marc Alff [MySQL] 00:01:26 PM, okay.
Can you hear me okay?
Tom Tan 00:01:33 Pardon?
And as I joined, but, They maybe went off just one minute ago.
Marc Alff [MySQL] 00:01:47 Okay.
I noticed that, zoom just gave me an error message, It wants an upgrade, so…
Tom Tan 00:02:01 Oh.
Marc Alff [MySQL] 00:02:02 Maybe that it will take some time to join, I don't know if he's affected or not.
Tom Tan 00:02:07 Yeah, I talked with him in the morning, I think. He's planned to… he was planned to join, but right now he's not in… In the office, maybe, for severe Image.
Marc Alff [MySQL] 00:02:19 Okay.
Since you're here, I saw that you have a PR related to views.
I have a few questions on that, if you have a moment.
Tom Tan 00:03:30 Yeah, sure.
Feel free to share your own question.
Marc Alff [MySQL] 00:03:48 So, in this issue, you mentioned that there is a crash due to memory corruption.
Basically, if I understand correctly, this is because we… the code does the wrong cast somewhere.
Tom Tan 00:04:00 Yeah.
Marc Alff [MySQL] 00:04:03 Could you… Did, could you clarify where that cast is? Just so I understand?
Tom Tan 00:04:12 I can paste the link, I think, just in the aggregation… Either Cafe or somewhere, because… Let me search it, I can, I can paste the line in the chat.
Marc Alff [MySQL] 00:04:25 Okay.
Tom Tan 00:04:26 There's a static cast. I think very easy to search, like, cast to one of the derived config there, but it does that bluntly.
Marc Alff [MySQL] 00:04:37 So it's when casting this subject, the aggregation config itself.
Tom Tan 00:04:41 Yeah, aggregation config itself, yeah, from base to the derived one, but the object is actually the base.
Not in the derivative one, yeah.
Yeah, yeah, it is quite a common pattern, I think, in the constructor.
For… for each of the… aggregation object.
like, long histogram aggregation, the constructor, the first thing is it can converts the cast, the… Aggregation pointer to… to that.
Concrete one.
Marc Alff [MySQL] 00:05:58 But… I'm trying to find that code, huh?
Tom Tan 00:06:06 You know, in the past, histogram underscore aggregation.cc, search that file.
Just the very beginning.
Merchant access dick. Yeah.
Marc Alff [MySQL] 00:06:34 Something like that.
I think so, yeah, we can open. Okay, should be the same for all the applications.
Tom Tan 00:06:44 in the constructor… Is it here? Search static cast?
Make mad.
Ehsan 00:06:53 Hi, Mark. Hi, Tom.
Tom Tan 00:06:55 Hi, yes, Anne?
Marc Alff [MySQL] 00:06:56 Bye, son.
Tom Tan 00:07:00 No…
Marc Alff [MySQL] 00:07:02 Application config.
Tom Tan 00:07:04 Maybe just open the histogram.
The other file, I'm not sure.
Pastegram aggregation here, this one.
Just here at 9. Okay. Yeah, like this.
Marc Alff [MySQL] 00:07:20 Or something like that.
Tom Tan 00:07:22 Yeah.
That are there.
Parameter can actually be there, be anyone, beyond, like, the base one. Base config.
Marc Alff [MySQL] 00:07:38 So… If we had to type… for each class, then I guess the… that code should check the proper type first before doing a cast.
Tom Tan 00:07:52 Man, we can add a check here, but this is our internal… code, right, once… and in the construction, like, when… in the construction of Vue, when we… It is made sure it is correct. I think here, no need to check, but I think we can also add a check here.
Because here, the aggregation config is already passed, I think, like, from the view, we stored it in our SDK, so once we validated it initially, no need to do… Nad.
Validation here.
Marc Alff [MySQL] 00:08:36 The part I don't understand is, so, adding a type like that the aggregation config this I get.
What I do not understand is, why is it… But we have those two parameters for the view.
And what do we mean?
Tom Tan 00:08:59 Oh, it's too fast.
Marc Alff [MySQL] 00:08:59 Greetings.
Tom Tan 00:09:00 is to a thing… I mean, why do we need two of them, not just one?
Is that the question?
Marc Alff [MySQL] 00:09:13 Yes.
Tom Tan 00:09:15 I see. I think for now, because the… Type, and Aggregation config is not a one-one mapping array, so we can't just pass in there.
Aggregation config, because config, there are much fewer config objects than the actual type.
So we have to specify the… 9.30, there.
Actual type.
Because many, many, many types share one config.
Marc Alff [MySQL] 00:09:48 But with that change, the aggregation config knows its own type now.
Tom Tan 00:09:54 Not very accurate, the hair. The hair, the type is just, like, the… It doesn't cover every aggregation.
Here, the config.
Because many aggregations share one config.
So, like, the base one, that is set to K default, that one is shared by… Quite, quite a few aggregation.
Because such aggregation doesn't carry out their own information, so it is okay for them to share their base one.
I mean, if we just pass… just, pass the… aggregation config object, and I don't… and, remove the aggregation type, the SDK, we will not know the actual aggregation type. We'll miss that, because from the config object, we can't deduce the exact aggregation type.
Because… Because when… The base config object can handle Like, many… Many aggregation. Aggregation.
But our SDK needs to know that.
Marc Alff [MySQL] 00:11:19 What… what do you mean by the base config object? What is that?
Tom Tan 00:11:24 Base, that's an aggregation config, right? That's a class name.
So that when…
Marc Alff [MySQL] 00:11:29 Yes.
Tom Tan 00:11:30 That's… that one is used by many.
That one is a concrete… that's not an abstract class. That one actually carries, like, the cardinality limit for now, and it works for… For many applications, which doesn't need, like, certain… their own… storing their own config data. So they just use a shared one, the common one.
Like, if you… if we count the… classes in the… in this file, aggregation config, I think that there are only 3 aggregation configure.
like, classes. But, for aggregation.
For the aggregation type, it is much more than that.
We don't create the aggregation config for for each aggregation, I think that's a problem. If there are one more.
Marc Alff [MySQL] 00:12:33 Well, should… should we vent?
Tom Tan 00:12:38 Pardon, or…
Marc Alff [MySQL] 00:12:39 Well, why don't we create a proper subtype for every aggregation config?
Tom Tan 00:12:45 I think we can, but maybe just right now, they're the same, maybe… We can't do that, that is… I think initially, we are not doing that. Maybe we can do that.
Even, like, for many of them, they're the same, because they don't carry out extra They don't need extra configure data.
Marc Alff [MySQL] 00:13:04 Well… Maybe those will not have attributes, but they will have a proper type.
Tom Tan 00:13:10 No.
Yeah, that's just one option, yeah, if we want to create Make them one-one mapping, like aggregation config and aggregation, then… Yeah, with, no need to… has to… That's true. But in that way, we change the SDK interface, right? Like, the user, when creating the view constructor, or… is exposed to user, the user needs to change the code. I think that's the part I want to avoid, like, with this VR, we need a user to change something.
change their SDK, even SDK, even… I think we don't guarantee their compatibility, but also… Don't want to break it… break it, sort of, with this change.
Like, view is constructed by the user, by the user.
Marc Alff [MySQL] 00:14:04 And then, yeah.
I'm still struggling to understand that, the… Passing two parameters that goes together.
Tom Tan 00:14:20 Yeah. It's very strange.
Alright.
Yeah, so, kind of, yeah, agree, yeah.
We can make them 1.
Marc Alff [MySQL] 00:14:41 And on top of that, I'm not sure I fully understand this comment from, from ChatGPT, but it's saying that… Assuming you have a distrogram?
It's actually valid to pass default, even if you have any strong RAM.
So… Vacczyk Wehr.
Will… will fail on default.
Even though, according to the review, it's supposed to be valid.
Tom Tan 00:15:13 Okay.
Marc Alff [MySQL] 00:15:14 I need food.
Tom Tan 00:15:18 Type equals… If it is histogram… Then… Nope.
If the aggregation type is histogram.
The user needs to pass in Instagram… aggregation config. Others will cause, like, Like, memory issue or memory?
Access issue.
The user can only pass in Giving aggregation type, a config type.
Marc Alff [MySQL] 00:15:59 Okay, so if aggregation type is histogram.
Tom Tan 00:16:03 Yeah.
So you could hide.
Marc Alff [MySQL] 00:16:05 It used to be.
Yeah. Yeah, but if aggregation is default.
Tom Tan 00:16:10 Yeah.
Marc Alff [MySQL] 00:16:11 they can't have an Instagram. I mean, this is what it's saying.
Tom Tan 00:16:18 Okay, sure. Between… between this line… Yep.
Marc Alff [MySQL] 00:16:24 Between… This line or this line, so 50 or 59.
This thing is saying that one of them is wrong, because you can also have an histogram with a default.
Tom Tan 00:16:41 Okay.
And let me double-check, face… Create a histogram with default aggregation, what does that mean? I need to double check it.
Marc Alff [MySQL] 00:16:51 Well, because this is in the view, the view later, this is default, it delegates to the instrument type to find the proper…
Tom Tan 00:17:01 navigation.
So does that mean, maybe the… The default aggregation type need to be… What? And then how to handle that case? Wondering.
Marc Alff [MySQL] 00:17:24 Well, I don't know, this whole thing is… needs clarity to understand exactly what is going on.
Tom Tan 00:17:30 Yeah.
Marc Alff [MySQL] 00:17:31 So…
Tom Tan 00:17:32 Okay, let me… Double check this… Hi, Lalit.
Yeah, I think he will join soon, Lalita.
Marc Alff [MySQL] 00:17:48 It disappeared.
Tom Tan 00:17:50 He just, shown up in the office.
Are you going to join the meeting?
Okay.
Okay, let me… let me double-check, and I will… I will put comment here for… for this one, and for the GPT comment.
Okay.
Marc Alff [MySQL] 00:18:13 So, in short, this thing… so, that part.
to prototype, so that every time we downcast that, it's safer. Yes, we can do it, and we should.
Oh…
Tom Tan 00:18:24 that will change the SDK API, right? So maybe if we want to do that, do that, you know.
future PR, you think maybe we'd discuss whether that deserves a break and change?
If we change, like, create… them config for each aggregation, then, like, we need to change the view API. Even the SADP, that's a freaking change.
Why?
I mean, we'll do that.
Marc Alff [MySQL] 00:19:06 What the full change would be, but… Right now, I don't understand that part.
It's too confusing. I mean, we don't know what each parameter is supposed to do and what it means.
Tom Tan 00:19:21 Maybe not, let me create a follow-up issue on this, maybe, and After this, I create an PR, maybe we can discuss the concrete code, maybe make it more clear.
Marc Alff [MySQL] 00:19:32 Yep, thanks.
Tom Tan 00:19:34 Okay.
Marc Alff [MySQL] 00:19:58 Isan, did you have anything special to discuss?
Ehsan 00:20:02 Oh, no.
Marc Alff [MySQL] 00:20:11 Okay, I took a… I took a few notes on what's going on in general.
one thing, so we can also wait for Tidy to join, but one thing I noticed is that in the specs.
There is a PR which is proposing to deprecate the Zipkin exporter altogether.
So, this is just for discussion right now, it's not a PR that is… so it's marked as do not merge.
But just to have a discussion.
And… I wasn't wondering if you have any, Comment on that, or if we… If we absolutely need to keep Zipkin for whatever reason, or if we can deprecate it.
from what I've seen, we don't have that many bug reports on Zipkin.
Which means it's hard to tell if it is just… Working exactly as it should, and everybody… everybody's using it and happy with it, or… Or to the controller if nobody's using it.
How to tell.
Tom Tan 00:21:32 Yeah, that's true. I think I haven't heard about, like, any… any issue reported on ZipKing, unless maybe sometimes there's build issue, or other.
issues on UTR repo.
And I did.
lalitb 00:21:51 Hi, hi everyone. Sorry. Hi, Lily.
Marc Alff [MySQL] 00:22:00 Yeah, so quickly, the spec has a PR to… Ask everyone if we can and should duplicate the Zipkin exporter.
Boom.
I did not reply yet, but… Oh… In my understanding, Zipkin is not very used.
And one thing that Zipkin does not support is, there is no authentication at all. There is no SSL, there is no… Note here, there's nothing.
So… I would guess that people are not using that, or if they are, people are not using that in production.
lalitb 00:22:43 Does, Jipkin backend support OTLP now?
Marc Alff [MySQL] 00:22:48 It's, it's in beta, not GA yet, but I think they went the same way as Jager.
Which is, instead of speaking the ZP nor Jaeger protocol to talk to it, they could accept all TLP.
So, if they do, we can… we can just use the… only the OTLP exporter to talk to the ziping backend.
Versue.
But, that will work, but, The PR in the spec just said that this is… still in beta, and not, not GA yet.
lalitb 00:23:25 Okay.
Marc Alff [MySQL] 00:23:30 So, if this is the case, I think we… Exporter itself.
If, especially if there is another way to talk to it with OTLP.
lalitb 00:23:45 I'm just having a bit nostalgic. This was one of my first PRs to act.
I think probably the first few areas of Phoenix Protection.
Yeah, but I agree, like, if…
Marc Alff [MySQL] 00:24:00 Yeah.
lalitb 00:24:00 If the OTLP is supported, I mean, even though it's beta, maybe, I think, good to start deprecating it.
Marc Alff [MySQL] 00:24:06 Okay.
So, depending on how it goes, For Jaeger, we just removed the code, because no one was complaining.
We can either do the same thing in… We don't know when, but we can either do the same thing or move the zip key exporter to contribute as well.
But, let's see first what, what the discussion is in specs to see if it's.
lalitb 00:24:41 Yeah.
Marc Alff [MySQL] 00:24:43 If it's deprecated or not.
Quickly on my notes, Cementing Convention has released, and I just did a PR last week.
to, to use it, so we are up to date with that.
On the configuration side, there is many… there's a lot of activity In the configuration repo itself.
To clean up things, and to… Get closer and closer to, to a 1-0, at least.
So, I probably need to do some small cleanup to adjust to that. Every time the… Every time the model changes, I need to change the… a YAML parser as well, to align with the model for that.
And also, on changes upstream, I just noticed that Proto did a new release.
1.9, which is too bad, because I just upgraded to 1.8.
So, we need to do it again.
although for that, because of the way it works for Bazel, we need first to wait for OpenTelemetry Portal to be available in Bazel Central repository, and then, only then we can use it.
in OpenTelementary CPP, so… quilt.
Probably take some time.
And on Weaver, Weaver made already this a while ago, and it's also used Together with the new Semantic Convention, so we are up to date on that.
Any other things you want to discuss in general?
lalitb 00:27:11 Not for my fault.
Marc Alff [MySQL] 00:27:12 No, okay.
Yeah, the next item is yours. Yes?
Tom Tan 00:27:20 And I have a question on the… on the config and… on the config of our SDK. Like, store our config to a header file.
During installation, I think we have an issue on that, right, for a long time.
Or… do you have any suggestions on this feature? I think I… I came across this issue, I think, recently, like.
Like, for us, we installed the… OpenTelemetry via VC package, package manager, which has, set, like, quite a few build configs.
And build that into library. And the user included the header file without knowing the builder type of flag set in this package, and then caused some inconsistency.
Marc Alff [MySQL] 00:28:11 Oh, you mean for the values?
compile flags? Yeah, like the standard library, such thing.
Tom Tan 00:28:19 Yeah, the user maybe detect this old friend library, and the inconsistent with our no STD lip, we… I think we… we depend on, like, AppSeal by default now.
That's a default.
But the user may compile with… The Visual Studio STO, then both are nothing compatible and of course, memory.
Accession issue, unless they… We no longer depend on Upsell, because we only use Upsell internal.
I think this episode is default, right? For us?
So we even removed that option with upsell.
Marc Alff [MySQL] 00:28:57 Yeah, I think it was removed entirely. The issue remains for the STL.
Tom Tan 00:29:06 Okay.
Marc Alff [MySQL] 00:29:06 And we still have some cleanup to do there, the… The problem is that… And it's in… First of all, we have a lot of D files which are used in other files, all of our.
Tom Tan 00:29:18 Yeah.
Marc Alff [MySQL] 00:29:19 And… When we install a package, we don't even have a file that says which define was used.
Tom Tan 00:29:26 With the configuration, yeah. Not to save it anyway.
And then the user interface better, right?
Marc Alff [MySQL] 00:29:33 Yeah, so we need to fix that.
Tom Tan 00:29:40 Yeah, like, this, like, caused the issue for the user, like, really.
Like, a runtime memory access issue, so very confused.
And I think we need to ask a user, like, to define some macro, or if they are not in CMake, and to work around. I think the ideal case is we generate, like, a config, opens or config.headerfile.h file, and the user… or our header file includes that at first.
Then, yeah, make sure… The config is consistent.
Between the users include? Yes.
Art and the library… Built Library.
Or you then install the library.
Marc Alff [MySQL] 00:30:30 of Follow… for the libraries, I don't think it's too bad, because either it is there or it is not.
But the issue, yeah, for everything which has a pontifine, in Edo file, -
Tom Tan 00:30:45 June.
Marc Alff [MySQL] 00:30:45 always can… can go wrong, I guess.
Tom Tan 00:30:49 Okay, maybe I will find out the issue, and maybe comment on it a bit, and .
Marc Alff [MySQL] 00:30:54 Nice.
Tom Tan 00:30:55 Oh, good.
Marc Alff [MySQL] 00:30:56 But yeah, wait till… It's an issue which has been there for a long time, but we need to do some cleanup if we want to be able to install a clean package at some point.
Tom Tan 00:31:07 Yes, okay.
Marc Alff [MySQL] 00:31:25 Okay, on the things to discuss in general, The last time we did a release was in September, I think?
Where am I?
Yeah, end of September, so… I think we… it's time now to… To make annuities.
any… do you have any special, PRs or bug that needs to be fixed?
Before we make annuities.
But you want, included.
Tom Tan 00:32:15 And, you know, I want to include, like, the current PR I'm making to the new release, if we're not, like.
Marc Alff [MySQL] 00:32:23 Also, they went.
Tom Tan 00:32:23 this one.
Marc Alff [MySQL] 00:32:24 The views.
Tom Tan 00:32:25 Yeah, the views, yeah.
Marc Alff [MySQL] 00:32:35 Okay, bye.
So, hold… Well, we start to… to prepare the release, I will, but I will wait for this, this PR anyway.
Tom Tan 00:32:52 Thanks.
Marc Alff [MySQL] 00:33:06 If we have some time, there are quite a few… Issues… That needs to be… to be discussed for triage.
So, this one is, yeah, what you… Which reported soon.
Which will be done… This one, so someone complains that when a span is dropped.
The reporter says that the trace should no longer be sampled.
And I'm not quite sure this is actually the expected result.
I haven't… I haven't looked at the spec in details, but in my understanding, When you have a sampler… when something is sampled, the entire trace is sampled, and no… No code can disable the sample flag in the code path.
So… We may forget to respond.
But dropping a span itself is not a reason to… Avoid simping.
So, this is… I haven't seen exactly in the spec where this is, described, this is my understanding. I wanted to check with you if this is your understanding as well, or if you know of what the expected behavior is.
Blood, maybe?
lalitb 00:35:01 I'm just reading the issue, process once throughout this parent, set it to active as parent.
It's something loop.
Not this twisted.
Starts with child span.
Custom sampler, which returns… I'm not sure, Process 1 and Process 2.
Returns, okay.
Check the child flag, trace flag, it should be true.
Why? I mean… I didn't get the question, actually. There are two different processes.
Two different processes.
Marc Alff [MySQL] 00:35:46 Yeah.
lalitb 00:35:47 One is… one which starts a span, Asparent.
Oh, it's propagating it to process 2?
So, these are client Line server, or what?
Marc Alff [MySQL] 00:35:59 Well, he mentioned processes, but I think this is just a parent and a child's plan.
lalitb 00:36:05 I don't think, because he's talking about propagate… Or is it doing something more in terms of child and client and server? I don't know.
Because it talks about two different processes, and then… Custom sampler. How can he create a child span with a custom sampler?
He will be creating… A new application with a…
Marc Alff [MySQL] 00:36:32 So maybe it's one process talking to another with a client server, and the server has an SDK with sampling.
lalitb 00:36:39 Yeah, so the one is a default sampling.
I mean, the process one, process 2 has a custom sampler.
Which result, which returns rock?
Marc Alff [MySQL] 00:36:52 To me, that just should drop the spine, not the trace.
lalitb 00:36:57 Yeah.
Check the child's band tree is black.
It should be true.
Oh, shit.
Marc Alff [MySQL] 00:37:06 No, it would be true. This is what he's complaining about, that the trace flag is still set.
lalitb 00:37:11 Okay, it would be true, yeah.
And… The child's been almost get the same.
Okay.
Oh, it's saying that.
Marc Alff [MySQL] 00:37:33 Because he's…
lalitb 00:37:34 Inherit the sampling decision of the parent one, irrespective of whatever the A custom sampler has… okay.
Fair enough.
I mean, to me, it looks…
Marc Alff [MySQL] 00:37:59 The good changes… Yeah, the code change he's proposing is trivial.
So it's only one line.
Basically… Basically, so… If something is sampled, we set the sample flag, and he's saying that, well, we should have an elsewhere, if something is not sampling, we should…
lalitb 00:38:25 remove the sample flag from there. So…
Marc Alff [MySQL] 00:38:28 Coding-wise, it's nothing. The big question is whether it is the expected result or not.
lalitb 00:38:37 Yeah, I think I'll also… I'll go through that. I think… difficult to… Find it from this, but let me go through the specs.
Ugh, what it's easier.
Did you reply something? I mean, or any discussion?
Marc Alff [MySQL] 00:38:53 Not yet, not yet, no.
lalitb 00:39:00 Fine, fine, I think I'll see the specs, and probably I will also respond, based on what I could make it for.
Marc Alff [MySQL] 00:39:38 Okay.
Oh.
This one, I didn't gut it, I don't actually get your question there.
Okay, well… I guess we have to… read your documentation and code, but let's.
lalitb 00:40:55 Oh, sorry, I think I was… I was respon… I was on mute, and I was responding, sorry.
Marc Alff [MySQL] 00:40:59 Awesome, yeah.
lalitb 00:41:01 So, baggage is a… is supposed to be a… is a non-mutable entity.
So… Which means that any operation, like sector delete, will create a new baggage.
And return, that's what I understand.
it should behave the same way as a resource behaves. Like, any addition we do.
Marc Alff [MySQL] 00:41:20 Okay.
lalitb 00:41:22 But let's see, just see operation, just… let's go down, probably set operation, what it does.
I mean, here only, like, in this API only, in the documentation.
Just go to the set, yeah, set… Record the value PMS report.
Gross.
Marc Alff [MySQL] 00:41:42 It's a yoga.
lalitb 00:41:44 Yeah, that's okay, right? Return the new baggage, so it won't modify it.
Contains a new value, so it will…
Marc Alff [MySQL] 00:41:50 Yeah, so typically the same thing as for context, I think.
lalitb 00:41:54 Yeah, yeah, same thing as context, yeah, sorry, yeah.
Marc Alff [MySQL] 00:42:00 Okay, so we should have a new baggage, and what he's saying…
lalitb 00:42:03 We are doing, right?
So it's a… it's a… it's a cost, right? It won't modify the current existing package, so it's good… it's fine to have.
Marc Alff [MySQL] 00:42:12 Yes.
So, it looks like we are doing the correct thing then.
Okay, I will double-check that and reply, so… but typically, this is the expected behavior then.
lalitb 00:42:39 Ew.
Marc Alff [MySQL] 00:42:39 So we have nothing to change.
This thing is just minor, I just discussed it with Duke already.
For some reason… VIN.
We just noticed that sometimes there is a double slash in a… in a path, where CMake says what he's… is installing.
But to me, it is purely cosmetic, because this means exactly the same thing as exporter slash promoters.
So, the same files are installed in the same place, and it doesn't change anything.
We discussed that a while ago, but, the DLL build for Windows is lacking a lot of, a lot of symbols.
You know, quite a few… Reports complaining about that.
So, so… This is a recent one, but we had something else also.
Yeah, so… What we're missing here is… where this thing is, I think it's there.
Oh, okay, I think it's this file.
Okay, so… We are presumably exporting things from the main SDK library itself, but we are not exporting things for OTLP… OTLP file, and so on, because I think those… That code is not, But define is not set in the makefile, so this thing is, is ignored.
And the installation test that we have for that are also… not covering it. So it's very likely that whatever DLL we build is actually missing a lot of parts.
Tom Tan 00:46:01 Dooming the… the… with OTLP file, it's not a different here.
Should…
Marc Alff [MySQL] 00:46:11 So I don't… I don't recall the exact details, I think it's, so we have installation tests for that.
Yeah, so very… The installation tests, just check that we have all the singletons, so logger, provider, trace provider, and so forth.
But they don't test that we have, the OTLP exporter, the… every… every part which is, conditionally defined.
Tom Tan 00:46:57 Okay.
Marc Alff [MySQL] 00:46:57 And I think… Vishu is…
Tom Tan 00:47:02 But the BDOP should not, like, depend on the test, right?
Marc Alff [MySQL] 00:47:25 Okay, I forgot where it was, but I've discussed this with Duke, and the conclusion was that the… The installation tests are not testing every part.
And… And we are likely to miss things when we… Link the library to export it.
Tom Tan 00:47:46 Okay.
Marc Alff [MySQL] 00:47:47 I'm sorry, I don't have the details in… I don't know.
But in, in general, Recently, I noticed that some people are trying to use the Windows DLL, I mean, for the single DLL with all the code.
And we have a lot of complaints of, many different symbols missing. There are also some complaints that this only works with ABI V1 and not with ABI V2, things like that.
Tom Tan 00:48:29 Yeah.
Marc Alff [MySQL] 00:48:35 So, likely a valid defect to… Twins.
Tom Tan 00:48:39 Some team told me, like, they… they added the ABI V2 support, but hopefully… We can upstream their change.
Marc Alff [MySQL] 00:48:50 Okay.
This I will double-check with Duke, but I think it's a usage issue.
And that the thing was actually working correctly.
Okay, so I will close that, because it's, It was a case of misuse of the CMIC script.
This one is also related to sampling.
So… If I understand correctly, they have an application, and they want to set the sample flag.
But instead of doing that externally from the SDK and samplers, we want to do that from the instrumented application itself.
And in my understanding, it's not meant to be done that way.
It's not up to the application to decide if it's sampled or not.
And if it's traced or not.
That he wants to… From the application code.
Set, set the flags in the trays.
Any, any comment on that?
Like, Lalit, my understanding is that we should.
lalitb 00:51:31 Sorry, I was… I was somewhere else, yeah, right?
Marc Alff [MySQL] 00:51:34 So, sorry, specify whether the sample is context.
lalitb 00:51:37 For root spans.
For now, when we start a Rootespan.
The sample plaque only can be controlled by always-on sampler, or… It, you know, passes ampliflex dynamically.
Oh.
Marc Alff [MySQL] 00:51:54 The question is, why would you?
lalitb 00:51:56 Yeah.
Yeah, the sample flag would be controlled by the sampling.
logic which is being… which… or the sample… the sample which is being used by this application, it cannot be…
Marc Alff [MySQL] 00:52:20 By the standing phone.
Yeah, my understanding from the spec is that it's not the application who can decide whether to sample or not.
lalitb 00:52:27 Yeah.
No, no, I think this cannot be done. This… this is not something in the specs here.
Marc Alff [MySQL] 00:52:44 Well, it's not in the specs, but it's not desirable either.
lalitb 00:52:47 Yeah, yeah.
Marc Alff [MySQL] 00:52:49 Okay.
Thanks for confirming, so I will reply to that then.
This is make file-related, some proposal from Doog.
I don't know the details about VCP package and module and whatnot, but That was to simplify the build.
So… It only affects the bit, it's not affecting the code itself.
And what… Tom, can you… look at that, because this is related to VC Package.
Tom Tan 00:54:05 Yeah, okay, yeah, I will reply this one.
Marc Alff [MySQL] 00:54:07 Yeah.
Okay, thanks.
And then we have some very odd things, so… I'm… A bit confused about the… the status for this, this thing, so someone complained about, optimization, okay.
then there's a PR for that.
Ex-advert, so, first of all, it's not building, but also… what VPR is doing… It's implementing a different circular buffer, but in test.
So, I don't quite get that. I don't know if this is just for prototyping.
to see the difference, because if a point is to change and improve the circular buffer, I would expect some changes to… The production code itself not to test.
So here there is a presumably better implementation, but it's all… this all lives in test.
And in any case, VPR seems to be dead.
Because I haven't seen recent activity on that.
No, this is from… Last action was from September.
these guys some benchmarks, so I guess we can keep the issue open, because if he found some way to improve things, all the better.
But to me, the PR is not ready anyway.
lalitb 00:57:05 Yeah, good evening.
Marc Alff [MySQL] 00:57:08 Okay.
And this one, a glass tissue. So… It looks like… Autoburf have some… global state, which is, in the process, which is shared for… by everyone using protoburf.
And this state needs to be cleaned up.
Where was that?
Someone, yes, so someone mentioned the proper API to call to clean up that static state, which is sticky.
But the problem is, I don't see where we can call that in OpenTelemetry CPP.
Because we don't know who else is using Protobuf.
Ehsan 00:58:19 And if we call that, we just kill everything else using protobuf, which would be a bad thing.
Marc Alff [MySQL] 00:58:24 And on the other hand, The problem for the cooling application.
To decide to call that or not, it implies that the application knows A protobuf is used or not.
So… when you define an SDK programmatically, if you use the gRPC exporter, you know that OWF is used, so we can… you can call that on shutdown.
But later, with a declarative configuration, where… the SDK is used, depending on a YAML file which is external.
The application code may not even know if protoperf is used or not.
So I don't see how the application can invoke this thing.
So it's a bit of… Unclear how to resolve that.
lalitb 00:59:35 I mean, how come this is a memory leak?
Is it that they are creating… Do you export it again and again, or something kind of like that, or…
Marc Alff [MySQL] 00:59:46 But this is what.
lalitb 00:59:46 One time… one time allocation and one-time deletion, right? Whatever is being initialized.
Marc Alff [MySQL] 00:59:49 Yes, yes.
lalitb 00:59:51 So…
Marc Alff [MySQL] 00:59:54 I don't think it's, it's creating an exporter or things like that. I think this is… I've seen something similar in a different environment.
Basically, So, the protobuf generated code, using the protobeth compiler, Contains some static initialization.
So, when you just load the code, there is a C++ object which is constructed.
That will register in some, There is somewhere a list of all the buff messages that exist in the process, just to… Keep the metadata for it.
And I think this is related to that.
lalitb 01:00:42 Yeah, I'm just…
Marc Alff [MySQL] 01:00:44 It's basically restoring… Like… Every file which is in the generated code is registering itself in a global registry somewhere.
lalitb 01:00:58 Yeah, I think I understand, but yeah, as you said, it's a bit… tricky, like, how… who should call it, I mean, like, whether we can call it or not, even though we are using Protob, with whether we are the only one who are using it.
that application.
So, application user knows that better if they can call it if they are using our library.
Marc Alff [MySQL] 01:01:24 Yes.
So, the leak is probably nothing, and especially if it's happening at shutdown, it's not… it's not an issue already in production, but I guess it can be annoying with Algon and whatnot.
Because, of course, you have false positives, and you don't know If it's noise, or if it's actually a bug, so… But yeah, a bit tricky. I don't think we should call that anyway, because it's too dangerous.
So the assumption is that somehow the application should know.
Ehsan 01:02:12 If we…
Marc Alff [MySQL] 01:02:13 use potato buff in the process or not.
And I have no idea if this thing is maintaining some sort of… Reference counter or anything, But it's.
lalitb 01:02:33 unlikely.
And then discussion started to move to GNU TLS now, or what?
Marc Alff [MySQL] 01:02:49 Yeah.
lalitb 01:02:52 Interesting.
Marc Alff [MySQL] 01:03:08 Okay, so…
lalitb 01:03:11 Yeah, I think I went to some.
Marc Alff [MySQL] 01:03:12 Can it clear?
lalitb 01:03:12 delete it. It should be called by the application.
After all the components, depending upon our shutdown, yeah, that's pretty much…
Marc Alff [MySQL] 01:03:21 Yeah.
And this is the tricky part.
So I guess at least that maybe should be documented.
lalitb 01:03:40 Hmm?
Ehsan 01:03:42 That's fine.
Marc Alff [MySQL] 01:03:48 Okay, so, yeah, in any case, not something we can do anything about, luckily.
The only thing we can do is document that better, so that people know what to do.
But likely, it should be in the main application code to shut down things properly at the end.
Oh, okay.
Yeah, so… With that, I have a better idea, so I will be able to comment on different issues, and… Possibly closer.
Ehsan 01:04:40 Oh.
Marc Alff [MySQL] 01:04:42 It's late already, but you have time to look at a couple of PR, maybe?
Shall we do that the next time? We already discussed the aggregation config thing.
Ehsan 01:04:54 Oh, laid bare away.
Marc Alff [MySQL] 01:04:57 I don't know if you noticed, but your PR is actually the oldest one by now.
Oh, well.
lalitb 01:05:04 Let me see, let me see what can be done. I mean, if I can't… if I want you to do that, I'll close it, I mean, I'm sorry.
Marc Alff [MySQL] 01:05:10 Yeah. So… Well, it can stay there, but that was a clever way to Who mentioned that the… the file configuration PR is, is done, and closed, and the issue.
lalitb 01:05:25 Yes.
Tom Tan 01:05:28 And the next oldest PR is from… from me.
And, yeah, we need, like, real initial, yeah, for the DL builder coverage, maybe still some gap there, yeah.
Marc Alff [MySQL] 01:05:41 And there's also still this UTF-8 thing for Morwent.
I think we need to take a look at it at some point to decide what to do.
the… The part which is scary to me is this, like, 1,000 lines of code.
go to TF8.
Okay, so… Yeah, so, we need to research this one. Those Copilot things, do you still want to play with Copilot and see what it does, or… I mean, should we continue with those PRs, or… and get a fix finally, or close them, or…
Tom Tan 01:07:13 Beautiful.
Well, Nali, do you have any suggestions?
Right.
lalitb 01:07:21 Pardon? Sorry?
Tom Tan 01:07:22 Copilot created a PR.
Marc Alff [MySQL] 01:07:24 The co-pilot things.
Tom Tan 01:07:25 Yeah.
lalitb 01:07:27 We have something from Copilot, sorry, I mean… Sorry about to…
Marc Alff [MySQL] 01:07:32 A while ago, this summer, you played with Copilot to see what it can do, but those PRs are still hanging.
lalitb 01:07:38 Oh, okay, sorry, yeah, I think it… We can close it, I don't think that we reached… to a logical… I mean… Making those logically ready, so probably we can close them if… Oh, let me, let me see, probably once.
Oof.
Marc Alff [MySQL] 01:08:19 Overall, this one is very small.
lalitb 01:08:21 Yeah, it should be straightforward.
Marc Alff [MySQL] 01:08:23 I don't see the… Yeah, so there was the CRA thing that was fixed.
Okay, well, I'll let you take a look. There's nothing urgent anyway.
Okay, so this one looks like it's deadened. This one… I think Lalit, you probably.
lalitb 01:08:55 Are you…
Marc Alff [MySQL] 01:08:56 comments, too.
lalitb 01:08:56 I have to look into that, I just got… there were some comments from Copilot, but I want to look into that. I mean, I was not very much… I don't want to be very much, I mean, to hurry on this, because this is… not a very generic use case, and I think it's kind of affecting the hot part.
Marc Alff [MySQL] 01:09:18 Yes. So, probably just want to spend some time and see.
lalitb 01:09:21 I mean, not…
Marc Alff [MySQL] 01:09:31 Okay.
So, this one… I saw some comments in the review about performances, but I don't think… I don't think… You replied yet? I don't remember.
lalitb 01:09:46 Who is this guy? Is he joining the meetings, or you haven't met him, actually?
Marc Alff [MySQL] 01:09:50 No, I see lots of problems.
Yeah, so I've never seen him in meetings. He has a lot of comments all over the place.
So, I think he's very motivated to… do something with OpenTelemetry, because he's really looking at a lot of places at once.
lalitb 01:10:08 Hmm.
Marc Alff [MySQL] 01:10:09 Whoever, My gut feeling when looking at the comments of the fixes is that, is… He's skilled, he knows a lot of things, but he doesn't know.
lalitb 01:10:24 The specs very much, and the background, so sometimes it can be a bit off.
Marc Alff [MySQL] 01:10:33 But it seems… that guy seems to be very motivated to do things in OpenTelemetry.
Which is good.
lalitb 01:10:40 Which is good here.
Marc Alff [MySQL] 01:10:42 Yeah.
For example, he has… he has a fix, in… in API, sorry, in API.
Yes, this one.
lalitb 01:11:05 Hey, alright, everybody.
Marc Alff [MySQL] 01:11:07 So… so there are parts where there is some cleanup which is, legitimate. Let me see an example.
Yeah, so things like that. This is… this looks legitimate and correct, so this is a fix for an actual issue, which is good, it's a good cleanup.
But at the same time, he's doing also other unrelated cleanups.
That can, break things. Like, for example… It changed the alignment of the structure. I mean, it changed the size of it. Before, it was 32 bytes, and now it changed that to… Size of whatever we put there, I don't remember what it is.
Yeah, this thing…
lalitb 01:12:04 Okay.
Wow.
Marc Alff [MySQL] 01:12:11 So… So… Those are things that, if we were to write the API from scratch today, those would be probably valid, but given that we have an existing API, It's dangerous to touch it, and it can break it.
So this is the kind of things, if you don't know the background, you cannot make that up.
Because, there are no tests that will check for that.
We know from history the reason behind things, but it's not enforced in test, and it's hard to… To find out, so… We have to… We have to see which things is valid and which thing cannot be used.
For example, he has a very good point that, some of those, This structure, for example, is just a basic class. It has no reason to have virtual, methods, so it's good to clean them up. And if we were to write the API from scratch.
It's better to do that as opposed to a virtual method. But now that we have some, I'm not… I don't know if we can safely… Remove them or not, because it will change the virtual table, and then the size of an object for that.
So, things like that, it's, So, overall, my impression is that he is killed.
So we need to… To comment and guide them in the right direction.
lalitb 01:13:54 Nope.
Marc Alff [MySQL] 01:14:16 So yeah, so it's basically… commenting all over the place, I mean… Shut point to an API.
some cool in SDK, things like that.
Which reminds me, this… so, we discussed this last time.
And… Since the decision was to change the… The token constructor to be, Protected only, so as I seem… Yes, ask, there for that PR to do some changes, but we have seen… have not seen any action, activity yet.
So, I guess I can ping him, or otherwise, I will just fix the… It's a very smooth thing, so otherwise I would just fix the PR directly.
With a comment, so that it can be merged.
lalitb 01:15:16 So, if we change that.
Marc Alff [MySQL] 01:15:20 Token constructor and disruptor to be… Protected only, it means that we still need that, that friend somewhere.
So that… that could most likely will stay, stay, and this will be, protected instead of being public.
So I think this is the… The safest change, because then it… it only allows token to be subclassed, but it does not… does not allow Any code to mess with it.
Directly. Which is better?
I think this is it for the PRs, I don't have anything special to… to discuss on… on those piers. I don't know if you have anything.
lalitb 01:16:32 Norway.
Marc Alff [MySQL] 01:16:33 Buyan.
Nissan, there's a, appear related to Docker, if you want to take a look. This is, Doog, proposing some cleanup.
to remove… Remove things that aren't… no longer apply, and most importantly.
to build all the Docker-related code with the… The dependency… the dependencies that we have using the tags, as opposed to use some old version number, hidden in the… In the Dockerfelder.
Ehsan 01:17:13 Okay, I'll take the loop.
Marc Alff [MySQL] 01:17:15 Okay, thanks.
I did a first review on that, it looks okay, but I know that… You know the girl much better than me, so… Oh, yeah, if you have a chance.
Ehsan 01:17:28 Yeah, sure, I'll do it during the week.
Marc Alff [MySQL] 01:17:37 Okay, any other things to discuss? It's… Otherwise, I will close the call because it's, it's getting late here.
Tom Tan 01:17:50 No from my side.
lalitb 01:17:52 Not surprising.
Marc Alff [MySQL] 01:17:54 Okay.
Thanks everyone for joining, man.
See you. See you soon.
Ehsan 01:18:02 So.
Tom Tan 01:18:03 Thank you.
Yeah. Talk to you later. Bye.
Marc Alff [MySQL] 01:18:07 Meh.
Bye now.
