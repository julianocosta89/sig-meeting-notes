SIG: Ruby SIG
Date: 2026-01-06
Duration: 60 minutes
Zoom Recording URL: https://zoom.us/rec/share/x2VcChYzKsC9P8uD0WyxgcONfoucdZ9nKO-DvYmX43QPPJvMT2zBNPT0SaZvaA7b.1hARRVAcHJVYBB2C
============================================================

## Zoom Recording Transcript

Kayla Reopelle 00:00:59 Hello?
Hannah Ramadan 00:01:04 Hey, good morning, afternoon, wherever you are.
Kayla Reopelle 00:01:09 Good day.
Hannah Ramadan 00:01:10 Good day.
Kayla Reopelle 00:01:17 Yeah, and Happy New Year. I hope people got to take some time off, and… Breast.
We'll give it one more minute, and then we'll get started, because Arielle had mentioned he wanted to join today, but,
I haven't heard anything.
Otherwise…
Hannah Ramadan 00:01:58 I saw him post an early seg,
the part looking for a review on some PRs that he had created.
Did some solid work there.
Yeah.
Kayla Reopelle 00:02:11 Also, my dog is chewing a bone behind us, so, if there's any, like, weird sounds going on, I apologize.
Hannah Ramadan 00:02:21 Zoom is weirdly good about.
Muting those sounds, yeah, I hear nothing.
Kayla Reopelle 00:02:26 Nice.
Alright, well, the spec sig was beefy today, so we can get into that a little bit, and then,
And then continue on.
So… yeah, there was a lot of stuff that people wanted to talk about today. I think that…
some of the most interesting things to us… hey, Ariel! Is… there's this…
Big conversation about, kind of, having…
the same sorts of mechanisms in every signal. And this came through with,
like, a opt-in metric advisory parameter. That was kind of the thing that started this conversation. And…
you know, leading into the idea of, like, wanting to maybe have advisory parameters for, for traces as well. It felt like a big brainstorming conversation, but if you're interested in, kind of.
how the SDK and the API can, evolve?
I guess, like, the next… the next phase of features, I think that would be a good conversation to go back and listen to.
Another conversation that could apply to us, but still feels like early days is, adding support for a distribution config in the config provider. The idea behind this that people suggested was almost to
create something in the SDK that can help configure instrumentation.
So that, you know, instrumentation config is kind of available anywhere.
there were a lot of security concerns raised by this, so I don't know if it's actually going to happen. But yeah, seeing as we have kind of our own config situation set up for instrumentation right now, that could eventually become, a break from the spec if that does go through.
Another interesting conversation was about, SEMCOM schemas.
So in this discussion, The idea that was put forth that really surprised me is that,
OpenTelemetry doesn't want to be the end-all, be-all for conventions.
They want to create, the ability to be flexible with, you know.
certain telemetry providers giving their own conventions, or, you know, whoever wants to ship that. And this is kind of a step in that direction, to have a new version of the SEMCOM schema, and kind of spec that out so that everyone could theoretically use this same structure, and then that would allow maybe, like.
Browsers in the future, the example was given to, have a key that they can build off of from the data, to have a tooltip that describes what that particular attribute is about.
And then instrumentation would more clearly ship what schema it is adhering to in a given version and iteration. So, I think this covers some of the conversations that we've been having, too, about, like, schemas and semantic conventions versions and the HTTP stuff.
But but yeah, but that could be an interesting one to revisit as well.
Another thing that we've talked about before in this SIG, I know Wendy's not here today.
Is adding some sort of, like, finishing completion method for synchronous instruments.
This is getting a lot closer. There are a few big blockers kind of related to…
I think, like, end times and tracking, like, the staleness of certain metrics.
There was another…
One… oh, and then, there was a suggestion for the SDK spec to also be added, but it seems like there's a lot of energy behind this right now, so it's likely, I think, that we'd have at least a spec in development for adding this feature pretty soon.
And then…
The last conversation was, you know, something that's kind of continued in different iterations since November. The,
the GC is interested in trying to, you know.
Bring the specification to stability, bring more of the language 6 to more stability in this overarching mission to
take OpenTelemetry out of its incubating project status.
So with that in mind, you know, there's some brainstorming. This was more just like an invitation, rather than an actual discussion of, perhaps
Figuring out how to work better with
the GC as SIG maintainers, to kind of collaborate on goals, to make sure that we're prioritizing things that are mutually beneficial, things like that, and possibly, like, ratifying that in a charter of some sort, which I guess is already
a charter for SIGS is already part of the OpenTelemetry bylaws, which was new to me, but they kind of proposed maybe reviewing these goals, you know, that we have for what we want to accomplish on some sort of cadence.
and just increasing, kind of, the sync points between SIGs and leadership. So, they want to hear more from maintainers.
If, you want to contribute to this conversation, and you're able to go to the meeting, next Tuesday, highly encourage you to do so. If you're not able to go to the meeting, but you have things that you want shared, I'm happy to present them on your behalf. Just send me, you know, the things that you want to discuss.
And then I can recap in the meeting afterwards in our SIG.
So, so yeah, really beefy stuff. I didn't, I didn't even cover all of it, but I think that this is what's, most relevant for us today.
Is there anything that people want to discuss in here before,
We move on from the specsig.
Hannah Ramadan 00:08:58 This one, the last one, has,
have we had any kind of, like, overarching direction given before, where, like, SIGs are kind of, like, in sync? I feel like usually it seems like it's been, like, just work on what you want, and, like, you know.
Kayla Reopelle 00:09:12 That's good.
I mean, not since I've been around, or not that I've noticed. I don't know, Arielle, like, you've been involved in the project longer, so maybe… it sounded like there was, more cohesion at the beginning when
signals were getting developed, and that it was like, okay, we're all gonna focus on traces, and try to get traces stable, and then go into metrics, and then go into logs, and it seemed like…
Ruby's project kind of fell off or lost the momentum when it…
like, at some point in the metrics, exploration. So, that's kind of where we're behind in trying to catch up.
But, but yeah, I don't know. Arielle, do you remember any sort of more… guided… Work, okay.
Ariel @arielvalentin (ATX, USA) 00:10:03 No, I think I mentioned this to you before, is that we… I think the big challenge that I see is that it's hard to keep up with the changes. So we don't know what we're missing, so we have to go through the process.
Kayla Reopelle 00:10:15 Yes.
Ariel @arielvalentin (ATX, USA) 00:10:16 of auditing. So, it was more, like, once we respect compliance for traces, we… Didn't keep the same energy.
I'm, you know… Bordeaux… I don't have anything else to add.
Kayla Reopelle 00:10:32 Okay.
Cool. Alright, well then, let's get into CORE. Thanks for adding some agenda items, Schwan.
Yeah, I started taking a look at this. I'd love to hear, what you have to say and what's going on on this one.
Xuan Cao 00:10:52 yeah, basically, The, the scale is, is,
Scale is shared, among different data points.
But they have different, attributes, so… It's very valid,
It was just kind of a serious issue, especially if they use, different, the data points
Yeah, and I think hosting is a lot of people's sum up, so I think a lot of people start using this stuff, so,
This is fixed, just to,
well, it's an initial fix that hopefully can resolve the issue, but I, I, I, I know there's more… there should be… be more to improve on, on this, expansion experiment.
But this one, just to,
I kind of, like, patched from the… Oh, these are the, This, contributor…
Brought up, so…
Kayla Reopelle 00:12:03 Okay, nice. Thank you. That, that's helpful. Is there anything in the implementation you want to go over together?
Xuan Cao 00:12:12 Oh…
Kayla Reopelle 00:12:13 Boom.
Xuan Cao 00:12:14 So, no, the only thing is, when I'm looking at other people's, no, other language, metrics, SDK,
Finally, it seems like…
Both Ruby SDK and Bash SDK use the hash a lot, use hash to store the… Data.
But for the RL SDK, they use, state to… Maintain… the…
What is current data point, and what is the period point, which is very different.
I'm not sure if we should spend time to…
Align with other, design, or we keep this, This kind of approach.
The only concern, probably just the memory usage, maybe Skype, because, yeah, you know.
But again, if they use,
If you use the cumulative application, then
then I won't say it'll be an issue, but, yeah.
Kayla Reopelle 00:13:34 Okay.
Yeah, I hear ya.
I mean, we're at this unstable phase right now, and it's complicated because people are using it, so we don't want to, you know, mess things up too much, but if there are big structural changes we want to make, it is probably easier to look at them now.
But we do have more… yeah, I don't know, but I think that's a great question that you pose, about the state.
Ariel @arielvalentin (ATX, USA) 00:14:04 But I mean, as far… you're talking about, like, the internal state of the exponential histogram itself, right, Schwan?
So rather than… Go ahead, please. Yeah, yeah.
Xuan Cao 00:14:16 And for all other, instruments, they also use the same kind of structure. They use the hash to store everything. For example, if you have, different, attributes, then that's, I…
A data point with different attributes is considered as a new Kind of an instrument, because
While you update the stuff, it…
Yeah, you update based on the different attributes.
Yeah, so we store everything inside of one hashh hash. For other language, we have,
They actually have different instances to maintain those kind of stuff.
Ariel @arielvalentin (ATX, USA) 00:14:56 So…
Xuan Cao 00:14:57 Yeah, that's… That's just the key difference.
Ariel @arielvalentin (ATX, USA) 00:15:03 So, when looking at this implementation where the mappings are using attributes, so…
If I'm… I don't understand all the nuances of this.
But when it's doing the attribute set.
Is the attribute set always the same hash key? Always resolving to the same hash key?
Xuan Cao 00:15:22 Yes, it's a Tenache.
Ariel @arielvalentin (ATX, USA) 00:15:25 Okay.
So, it will always find the right mapping to apply. And is this exponential histogram bucket class?
Is this a fiber safe class?
Because it uses instance variables, so it's just getting, like, one instance per… instrument, I guess?
I don't know… I don't know what the… I don't know enough about the Metrics SDK to know.
Xuan Cao 00:15:56 Sorry, which part?
Ariel @arielvalentin (ATX, USA) 00:15:58 So, like, alright, so the exponential histogram, what is the…
you know, maybe this is a question that you and I can discuss offline, but I'm wondering about… I see that, for example, this uses instance variables.
So, and the hashes themselves, there's no locking around accessing these hashes.
Is that a problem?
Xuan Cao 00:16:24 Oh, you mean for the mapping instance?
Ariel @arielvalentin (ATX, USA) 00:16:26 Yeah, yeah, for these mappings, yeah.
Xuan Cao 00:16:30 Oh, I think Magpin is actually the hash.
Ariel @arielvalentin (ATX, USA) 00:16:34 That is…
Xuan Cao 00:16:36 contain… List of, mapping?
Matt Castle. That is… Distinguishable by the different attributes.
Oh…
Ariel @arielvalentin (ATX, USA) 00:16:48 Yeah. But this class, like, I see so much usage of it, so it's deleting things, it's adding things to it, it's clearing the mappings out, and this is in the bucket itself, the bucket object.
So is that bucket object scoped?
one… When the users are interacting with this exponential bucket histogram class object.
Do they have thread-safe access to it, or fiber-safe access to it?
You know, this might be something I need to, like, spend time understanding. It's hard for me to provide a code review that…
Maybe I should say that instead.
is I would love to review this, but I don't know anything about… That's the case back.
Kayla Reopelle 00:17:40 Yeah, it's a lot. But, yeah, those are, those are good questions.
Ariel @arielvalentin (ATX, USA) 00:17:48 Is there anybody else that we can leverage for the SDK spec reviews?
Like, do you go to the metric sig?
Xuan Cao 00:18:01 No, no, I didn't go to Metro Street.
for the, for the spec, to align with spec, I, I mostly just,
For us, just take a look at what current stack say, and then do…
make sure this, and also just look at other people, other large SDK to, to,
To make sure they are alive.
Ariel @arielvalentin (ATX, USA) 00:18:26 Yeah, yeah, absolutely. Absolutely. I think for me to be able to say, like, oh, I agree, I understand this implementation.
I have to personally understand the nuances. So, since we don't have anybody else who's an expert.
Here, in this group.
on the metric SDK, I don't know if there's somebody from outside our SIG that might be able to help us.
like, maybe somebody from the JavaSig can look at it, and… or, you know.NET SIG or something, or even the GoSig, like, if there's somebody who implemented metrics there, that they can double-check
Or, I don't know if even Carlos, you know, from the spec team can take a look and see if they might be able to… because he did the…
The certification for us for the, you know.
That we… that we satisfied the tree spec.
I'm trying to unblock you, is what I'm trying to say, Sean.
Yeah, because otherwise, I'm gonna keep asking questions like, is this thread safe? Is this fiber safe? Is this the right thing to do? Like, I don't know. I'd have to spend a lot of time kind of, like, knowing the…
Knowing the scope of things myself. Does that make sense?
Xuan Cao 00:19:32 Yeah, it definitely makes sense, yeah, yeah. And also, regarding this, is this, like, is this… is this everything, is everything stressed safe? I can double-check,
Yeah, but… Yeah, I can double check if there's a stressor.
Ariel @arielvalentin (ATX, USA) 00:19:49 Cool.
Thank you for your patience.
Kayla Reopelle 00:20:04 This one… exemplars updated, that's awesome. Thank you for that.
Xuan Cao 00:20:08 Yeah, so, I opened for review last time, but then I realized, it's, it's really out of our bag,
So I, before the new year, I updated, everything to make sure they are, aligned with spec as our spouse.
And also take root of efforts from Launch SDK to make sure they are the… they're, they perform the similar,
Yeah, so now it's, I think, ready to review.
Kayla Reopelle 00:20:42 Okay, awesome.
Thank you. Yeah, it has been a little bit since I've re-read the spec, so it's good to know that it's been updated. Let me take a look here.
Alright, anything else in CORE we want to discuss before we move on to Contrib?
Okie dokie. So… Arielle.
Ariel @arielvalentin (ATX, USA) 00:21:15 Somebody wanted to contribute another instrumentation for a library named Rage RB.
It's very comprehensive.
So, it got me thinking about the problem that we have, which is, in order for us to accept things into contribib, I think…
Even though the instrumentation API still is not really stable, I feel very much… concerned.
That, we don't get… we don't have enough capacity to…
maintain the existing contribib instrumentations ourselves.
And so, especially in cases like this, where…
someone who's a core contributor of the library, so this person, submitted this instrumentation. The suggestion I made was, hey, it would be much better
If you built OLTEL support into the library yourself and maintained it.
Because you're the expert, and then you don't have to wait on us
To say, yes, we approve, and merge, and whatever.
to get it rolled out as part of the bundle. We could work with them to say, get it registered in the registry.
In the hotel registry, and ensure that, like.
If they were to use ALL, or if they were to use…
the operator, hook that Schwan has been working on.
That those libraries are also loaded and auto-instrumented, right?
So I think that that's something that we can offer, and we can work with people on.
But I think from going forward, unless it's, like.
some really popular library like Faraday, or some really popular framework like Rails, I don't think that we want to continue to accept contributions.
To contribute, and try to steer people to just say.
Go ahead and build the instrumentation.
And keep it as part of your repo.
We… and again, we'd be happy to help you.
kind of how I feel about it right now. And I just want to find out if other people feel the same way, or am I just, like, am I barking up the wrong tree here?
Am I… pushing people away incorrectly, or… I don't know.
Kayla Reopelle 00:23:41 Yeah, I thought this was a fantastic response, and really aligned with, our ultimate goals for OTEL, and so why not kind of start the process now? We had a little bit of this when we were working with
read on the semantic logger stuff. You know, he was the maintainer of the project, he was interested in having a bridge, and now he knows more about OTEL and is maintaining the bridge, and, knows that he can reach out to us for support.
I think, yeah, being able to just be an hotel resource.
for Ruby Library authors, would be much better than kind of taking
the control of the project out of their hands, unless it's a very…
core library, yeah, like, I think, like, Rails and…
If we… if we have a maintainer engaging,
That feels like a no-brainer, to ask them to just move the work into their own project.
And… I wonder if, like, we could…
In all of the time that we have, at some point, make a document that might, like, help
maintainers of other libraries get started? Or just know, kind of, what resources we would point people to, to make it easy for them to have this,
This going, you know, like, how to get set up with the hotel registry, things like that.
that's the only extra async resource I think of when I'm reading this as something we could potentially provide, but but yeah, not needing to learn about…
the intricacies of rage and really question, you know, what needs to be monitored and how it should be monitored. It… it…
it seemed… I love the idea of, yeah, not adding another instrumentation and really focusing on maintaining well the instrumentations that are key to the Ruby community until we get to a point where we could also move those into their gems as well.
And I love that he's amenable to it. That's exciting.
Xuan Cao 00:26:08 I think one good example is Elk Search. They actually.
Kayla Reopelle 00:26:11 Dude.
Xuan Cao 00:26:13 they are… They have everything inside there, you know, such true.
The only thing I complain… I don't complain is that I don't know…
I think it's a lot of spec, but their, instrument and scope name is undifferent.
This is the only thing that happens is different.
Other than that, I think it's pretty, solid, instrumentation library.
confused.
Kayla Reopelle 00:26:47 Nice. Yeah, and maybe that's an opportunity, you know, if we see things like that, to open a pull request on those repos and see if it makes sense to change it, or what that friction would be.
Ariel @arielvalentin (ATX, USA) 00:27:00 Okay, so I think what I'll do is, in the instrumentation guide, what I'm gonna…
do is make something very clear and explicit, which is, essentially, we're not going to accept any new instrumentations, except for things that are related to the core Ruby runtime.
So, things like NetHTTP, Stuff related to the built-in logger, things that are part of, effectively, like.
Ruby Standard Library.
Kayla Reopelle 00:27:29 Hmm.
Ariel @arielvalentin (ATX, USA) 00:27:30 And we're gonna continue to maintain the things that we've got.
you know, Faraday and, so on and so forth.
But we need to start heading towards a direction where we're…
Eliminating some of the things that we are maintaining.
And I have sort of, like, an expiration date on stuff.
Kayla Reopelle 00:27:51 Yeah, yeah, I think that makes sense.
And, you know, check in in places, where we don't have…
community members who are willing to maintain things? Because I guess we run into one other problem where, you know, what if we can't get a maintainer of the library to add instrumentation, but a community member really wants instrumentation, then what do we do?
Ariel @arielvalentin (ATX, USA) 00:28:18 I think in those cases, it's like,
again, if the… the core library… I would take Rails as an example. Like, I don't know…
If we would ever convince the rails community to take on first-party instrumentation, right? That's why they had, like, all these hooks.
put in place.
So, in those cases, I think we continue to maintain those as part of our Contrib repo.
And in fact, you know, it might make sense to eventually break it off and have…
just an instrument… a Rails instrumentation repo on its own.
Kayla Reopelle 00:28:54 Hmm.
Ariel @arielvalentin (ATX, USA) 00:28:54 But,
But that's what I mean, it's kind of like, we… if we run into another situation like that, like, let's say somebody says they wanna…
do an army, or something.
and the folks don't want to maintain Hanami, well, we can look at it from a scale of popularity as well.
Like, is it receiving… is Hanami receiving updates? Is it… you know, what's its, like, usage?
Right? Because one of the things that we don't want to do is grab,
a fairly unknown library, I guess?
Kayla Reopelle 00:29:34 Yeah.
Ariel @arielvalentin (ATX, USA) 00:29:35 that doesn't have a large user community, and then included in the REAP, want to have to maintain it and have a sunset process for it.
Kayla Reopelle 00:29:40 So I think.
Ariel @arielvalentin (ATX, USA) 00:29:43 not… I think I'd be biased to…
Biased in favor of very popular libraries.
But I still would want to try to negotiate with the maintainers if they can…
Included as part of their journey.
Kayla Reopelle 00:29:58 Yeah.
Ariel @arielvalentin (ATX, USA) 00:29:59 this instrumentation, this first-party instrumentation of part of their job.
Right.
Kayla Reopelle 00:30:04 Yeah, I think that makes sense.
Ariel @arielvalentin (ATX, USA) 00:30:08 So, I can say, case-by-case basis.
Kayla Reopelle 00:30:11 Yeah.
Ariel @arielvalentin (ATX, USA) 00:30:11 of cover…
Kayla Reopelle 00:30:15 Because I'm… yeah, I guess the other thing is, I'm thinking about, like, GRPC, last year, where we got to a situation where
The person who made it wasn't going to maintain it, but there was a community desire to have GRPCs, so we just kind of migrated the gem over. That wasn't a very painful process once we figured out who to talk to.
in Ruby Gems.
But,
Yeah, I guess I'm just saying that as an example of something that we could encounter in the future, if…
we run into that problem, but I guess, yeah, we'll cross that bridge when we come to it, and I think this is a good policy.
Ariel @arielvalentin (ATX, USA) 00:30:54 Yeah, if people really want the instrumentation, then they'll… Volunteer to maintain it.
Kayla Reopelle 00:30:59 Yeah, yeah.
Yeah, and then people can look at the authors and see, okay, is it OpenTelemetry maintaining it, is it someone else who's maintaining it, and kind of make that choice on their own.
Ariel @arielvalentin (ATX, USA) 00:31:10 No.
Until such a time that we figure out a way to do automatic instrumentation without writing any code.
Kayla Reopelle 00:31:18 Yeah, yeah.
Someday.
Ariel @arielvalentin (ATX, USA) 00:31:22 EBPF, here we come.
I'm joking, folks, Logan.
I didn't mean to make… I didn't mean for this to linger so long, but thank you for confirming.
Kayla Reopelle 00:31:34 Yep.
Yeah, you have a good cue of PRs, this is helpful to see them all lined up like this.
Is there anything…
Is it kind of, like, bottom to top you want prioritized for reviews? Are there certain PRs?
I know we're, like, pretty close on that SEMCOMF PR, I think that's the right one. My…
My memory of… the before is still kind of foggy.
Ariel @arielvalentin (ATX, USA) 00:32:08 Yeah, so the… where we last left SMCOM PR was, we were gonna leave it at version 117.
Kayla Reopelle 00:32:15 So that's what I did. I left it at version 117.
Okay.
Ariel @arielvalentin (ATX, USA) 00:32:20 For the… the next ball up is the SQL comment propagator.
So, if you look back… If you look at the… Implementation?
it's adding… a utility, to,
the SQL processor to add the commenter, which is gonna be similar to
Similar in functionality to the Google SQL commenter, or the Vitesse commenter that we have here.
Which is essentially, like, keeping the pattern, or, like, an interface of a… Context propagator?
Except the thing is not necessarily injecting
The thing is manipulating the string, the SQL string.
And appending it to the end of the string per the specification.
So… It doesn't intentionally leverage
Things like active record query logs, which it could have.
But I intentionally did not do that, because that would make it specific to ActiveRecord.
Kayla Reopelle 00:33:38 Yeah.
Ariel @arielvalentin (ATX, USA) 00:33:39 And so…
you know, it's handling the circumstances, like, if it's, you know, for frozen strings, what do you do, and so on and so forth. All the values have to be URI escape, so…
You know? I try to figure out, like, is there a way for me to reuse things like the baggage processor, which has the same similar syntax?
Okay. And didn't find an easy way to do that.
But I think I've hit all of the…
all of the use cases that I could think of with this.
Kayla Reopelle 00:34:20 Nice.
Ariel @arielvalentin (ATX, USA) 00:34:23 And I put it in the SQL processor gem, only because I felt like
the processor is attracting things, like, we're changing things, or extracting things, or evaluating things about an SQL statement.
Which is why I felt like that was the best place to put it.
Kayla Reopelle 00:34:42 Yeah, I… I agree. I think that's… it's a good use of that new gem, so that we can get all of that shared logic in one spot, and…
Ariel @arielvalentin (ATX, USA) 00:34:50 Yeah.
Kayla Reopelle 00:34:51 distribute from there to MySQL, PG, Trilogy.
Ariel @arielvalentin (ATX, USA) 00:34:54 Yep.
Kayla Reopelle 00:34:54 So.
Ariel @arielvalentin (ATX, USA) 00:34:56 If your preference is to split it into multiple PRs, I'm amenable to that as well. I just figured that
Seeing them all together, one kit in the kit and caboodle, where it's like…
Here's the commenter, and here's the actual usage in code somewhere.
Kayla Reopelle 00:35:17 Yeah, I'm good with reviewing it as 1PR.
Ariel @arielvalentin (ATX, USA) 00:35:19 recall.
Kayla Reopelle 00:35:22 Does anyone else want it in multiple PRs?
Hannah Ramadan 00:35:27 I took a… oh, yeah.
Go ahead, sorry. Oh, I was gonna say, I took a look at that maybe 2 weeks ago, and I thought it looked pretty good. And I like that it's in the SQL processor jam, I think that makes sense, and it's nice to build that out.
Ariel @arielvalentin (ATX, USA) 00:35:40 That's your baby right there.
Hannah Ramadan 00:35:43 gross.
Ariel @arielvalentin (ATX, USA) 00:35:48 So, the… that one is me going through the test suite and saying, man, we have a lot of appraisal files that aren't.
Kayla Reopelle 00:35:56 Mmm…
Ariel @arielvalentin (ATX, USA) 00:35:58 set up right? Or, like, are…
are missing cases, right? So this is, like…
Adding additional test coverage, removing things that are no longer supported,
Adding… just making them a little bit more symmetric, because it's like, oh, as we add new minor versions to cover in appraisals.
Put them in a loop. Like… And where it's missing?
Add a appraisal for a latest version of something.
To try to get us closer to…
Having better test coverage for different versions of… You know, things.
Nothing really special about this other than something's failing, and I don't… I haven't looked at this in a couple of days, so I don't know… what it could be.
Kafa?
Kayla Reopelle 00:37:00 Kafka, who knows?
Ariel @arielvalentin (ATX, USA) 00:37:03 Oh, you know what? Is this the problem that I reported?
Oh, no, this is me with my RoboCop stuff. Can't you just autocorrect RuboCop?
Kayla Reopelle 00:37:12 Come on.
Ariel @arielvalentin (ATX, USA) 00:37:16 Sorry, I'll fix that.
Kayla Reopelle 00:37:17 Cool.
Thank you so much for doing this. That's, that's really helpful and good to audit.
All of that stuff, and get it… get it taken care of.
Ariel @arielvalentin (ATX, USA) 00:37:27 I don't know what else to do with my time other than try to do this stuff.
Because it's like, they're all, like, little annoying chores that I send to…
Kayla Reopelle 00:37:39 the co-pilot agent, like, threw this for me.
Ariel @arielvalentin (ATX, USA) 00:37:43 And then see what it produces.
Which is often revert and try again, I didn't give you the right context.
So again, it's like, as we're moving… the one that you were just hovering over is a little bit funky… is a little fun.
So one of the problems that Dependabot had is that it couldn't…
run to update dependencies anytime I found a gem file that used a local path.
Kayla Reopelle 00:38:11 Mmm.
Ariel @arielvalentin (ATX, USA) 00:38:12 So… and RenovateBot can't do that either, so a way around that…
was to use a feature in Bundler, which is point to a Git repository, and then set your bundle config…
To point to a local repository instead of a remote one.
Kayla Reopelle 00:38:30 Hmm.
Ariel @arielvalentin (ATX, USA) 00:38:33 So… I did this, for example, like, I was like, hey…
Base is gonna be… there's base gem spec, whatever, but when you run this script, local dev on your local machine.
which is the script after it, up to Ben.
If you run this script, it'll go through every directory and set your bundle config to use the local repo path instead of the remote one.
That way…
Kayla Reopelle 00:39:05 Cool.
Ariel @arielvalentin (ATX, USA) 00:39:06 This is super hacky.
So, like, this is a way for me to say, I could still use local Git files, have them get updated, and you can see them.
But then… I can have Dependabot run, and it try to update the dependency version numbers properly.
How's it going, man? Hey, there's a hook in one of those jars there to open up the lid. If you look on the left, sorry, under… give me one second, y'all. No, not right here.
Kayla Reopelle 00:39:56 A lot of gem files.
Ariel @arielvalentin (ATX, USA) 00:40:16 Yeah, I'm real sorry about that. So I would love it if, when y'all are reviewing this, to try it on your local machine, or your Codespace, or…
You know, your virtual machine, whatever it is you use for development.
Give it a try and see if it works.
R… Because it worked on my machine, worked on my Codespace.
That's not enough testing, I don't think, because it always works for me.
Kayla Reopelle 00:40:41 Cool.
Yeah, I like this idea as a workaround, and I'll give it.
Ariel @arielvalentin (ATX, USA) 00:40:47 Yeah, because then we can have her renovate actually update all the gems right.
Yeah, definitely. Can't do right now.
Kayla Reopelle 00:40:54 Really nice.
Ariel @arielvalentin (ATX, USA) 00:40:57 I gotta… Seaspells, seashores.
Okay, so ActionView didn't really have any test coverage in it, and this is where I broke the mold.
Because what I wanted to do with Action View was add, like.
We have a very strict policy.
Folks watching on… out there. Know that at GitHub, we have a very strict policy, so we have,
attribute processors, and Transform processors are running them in collectors.
And any data coming from any instrumentation at all.
Has to go through a classification filter.
And what's happening is because we rely on upstream SEMCOM and namespacing to say, like, hey, http.statuscode
Yes, you can collect that attribute. Why? Because it doesn't contain any personal identifiable information or any customer
Private data at all, right?
No sensitive data in it.
So, yes, allow HTTP status code through.
Or, if it's some other random attribute, you drop it. We have a redaction processor that drops it, but it reports, oh, by the way, this attribute was sent through, but it was redacted. It shows up in the redaction…
Tuple, or the, you know, attribute list.
And, the names that Action View Instrumentation uses are very generic. It's like Identifier.
And something like that. So I'm like, okay, well…
Those attributes may not be great.
For what we're trying to do, for what we want to do, which is…
to have them namespaced around Rails or Action View itself.
And then I looked at the test suite, and I said, holy crap, this thing doesn't have any tests.
So I started writing tests for it, only to find that mini-test spec doesn't work very well.
at least with what I was trying… with what I was trying to do, it was very, like, complicated.
So this is the case at which I have broken the normal…
path, because Minitest spec itself does not provide out-of-the-box integration with Rails. There's a separate gem called Minitest Rails, and I did not want to add an additional dependency here.
Because I want to stay ahead of these other libraries so that we can continue to test
of rails itself, so… If you look at this.
test suite now for Action View here. I've added test coverage, but it's using the Action Controller test case features.
so that I can render templates,
Not exactly run-up, it'll execute the code, and then have it go through the notification system.
And I can start looking at these attributes. So I first wanted to start adding test coverage.
before going through and saying, okay, now we're gonna apply SEMCOM and start naming these things something.
So that other PR that I had, which was, here's the documentation, here's what the instrumentation omits now.
Because I want to propose a breaking change to say, we're going to rename these attributes.
Schwan gave me one pass already, and of course, like, I made really silly, sloppy mistakes in there, and thanks for his review, I've cleared those up, so he can give me another…
Look at his fun, I'd appreciate it.
God, there's so many, I was busy, right?
Kayla Reopelle 00:44:53 January! You're getting a lot done.
Ariel @arielvalentin (ATX, USA) 00:44:56 Not that any of it advances metrics, but…
Kayla Reopelle 00:44:59 Cleans up other stuff.
Ariel @arielvalentin (ATX, USA) 00:45:02 Yeah, so… The one act of this is a result of the one…
of me trying to upgrade to Ruby 4. So what I learned here was, we did not have Bundler set up right anywhere.
Whereas we had… we were referencing, like, different versions of Bundler… sorry, we're referencing versions of Bundler that will only work with Ruby 3.
And now that we're trying to upgrade to Ruby 4, the bundler version doesn't match.
But Blender already comes with Ruby Gems when you install it, by default, so… what's the point in declaring it if it's already there because you installed Ruby?
So I said, I'm taking Butler out of the gem specs, because they're only used for tests.
I'm really glad that you did this, because I've thought about it a couple of times, and then always been like, there's something else more important to think about right now.
Kayla Reopelle 00:45:55 I'm glad that eventually the wavelength collided.
Ariel @arielvalentin (ATX, USA) 00:45:59 I have your attention anyway, I guess. Even though you didn't want to think about it.
Kayla Reopelle 00:46:04 Yeah.
Ariel @arielvalentin (ATX, USA) 00:46:05 I got you thinking about it.
Kayla Reopelle 00:46:06 Yep.
Ariel @arielvalentin (ATX, USA) 00:46:08 And then the.
Kayla Reopelle 00:46:09 Oh, just one more thing on this, because I went back in time, to see why Bundler was added, and… because it's all present in the SDK as well, and it looks like it was just part of the default gem set that was added in the template. It's never been called specifically or used in that way, so…
Ariel @arielvalentin (ATX, USA) 00:46:28 We can do this cleanup on the SDK, too.
Kayla Reopelle 00:46:33 Okay, those are my two cents.
Ariel @arielvalentin (ATX, USA) 00:46:36 joke.
Kayla Reopelle 00:46:36 Last one you want to talk about?
Ariel @arielvalentin (ATX, USA) 00:46:37 And last but not least, I added test coverage for Ruby 4.
And it's dependent… it's dependent on these other things. Here's some stuff that you would like to know. Is that loggers no longer included in Ruby?
Delayed job, we rely on the test helpers in delayed job, and those rely on Ostruct, which are not included anymore.
In Ruby?
The Gruff library does not have any support for Ruby 4, so the tests don't run.
Rack, we… had tests covering a bunch of cases for things that aren't receiving security updates.
And so I removed them.
Kayla Reopelle 00:47:20 Nice.
Ariel @arielvalentin (ATX, USA) 00:47:20 And similar with Sinatra, Sinatra is, like, super permissive about what version of rack you can use.
So what I did for Sinatra… let's take a look.
you can always type Sinatra in that little filter file.
Yeah, there you go.
And so for Sinatra, what I did was this little hacky kind of thing, which was… Anything before 4?
Add it to that loop.
So it's like, we, you know, you have the code that kind of loops through and says, generate appraisals for each of these versions.
I said, yeah, I'll do this hacky little thing, which is, like, it's not really a force, I'll add these. And that's about it.
Because Ruby 4 won't support 3-2 or 2-2.
Kayla Reopelle 00:48:17 Nice.
Thank you, thank you for doing this. Thank you for getting us moved over.
Ariel @arielvalentin (ATX, USA) 00:48:26 Getting you more work to do.
Kayla Reopelle 00:48:29 This is… this is easy stuff to review. This is… this is my breaks from relearning what exemplars are.
Ariel @arielvalentin (ATX, USA) 00:48:36 So…
Kayla Reopelle 00:48:38 We'll have a good little hotel day today.
Let's see, what else?
Ariel @arielvalentin (ATX, USA) 00:48:47 I don't think that… I think that was it. I don't think I have anything controversial.
Kayla Reopelle 00:48:52 Cool.
Ariel @arielvalentin (ATX, USA) 00:48:52 Like I did the last few times.
Kayla Reopelle 00:48:58 Alright, ready to move on?
Got one more.
More point.
Ariel @arielvalentin (ATX, USA) 00:49:04 the operator.
Kayla Reopelle 00:49:06 Haha!
Ariel @arielvalentin (ATX, USA) 00:49:07 This is the one we've been waiting for.
So, Sean, I… I don't know if I can commit to going one more pass through here.
what I would be doing in my review is looking at Just kind of, like.
Silly… being silly and, like,
You know, looking at idiomatic things, or whatever.
I see that in some of the cases, you said… you had called out that, like, RoboCop, like, using Warren better than, say, standard error puts.
You know, totally fine with me.
And we give it to the gods.
The one thing that I do want to do is figure out a way to test this.
Are you testing this using something like Kind, or something like that?
Do you have, like, a…
Xuan Cao 00:49:55 Do you mean, like, unit tests, or, like, actual doctor testing?
Ariel @arielvalentin (ATX, USA) 00:50:00 Like, actual testing, yeah, like, like, doing exploratory testing, like, trying to…
install this gem… well, I guess… I guess this gem would…
Because the CRDs are not here, right? The CRDs are in a different repository.
Those are in the Open Telemetry Helm charts repo, right?
Xuan Cao 00:50:30 Yeah, yeah, I actually do a test, with everything, like, by,
Because I already have a PR, like, all the stuff that I pushed for the open telemetry operators, and then I basically, from
From that point, I, I just,
do as, like, normal guy to start using this stuff, and then I think I have a video to show, what it looks like once, .
Ariel @arielvalentin (ATX, USA) 00:51:00 Was that in the description?
Xuan Cao 00:51:02 No, I think it's in the open time to operate a PR. I can, share that.
We do.
Kayla Reopelle 00:51:09 We could add it as a comment or something, or in the description.
Xuan Cao 00:51:12 Yeah.
Kayla Reopelle 00:51:12 really helpful.
Ariel @arielvalentin (ATX, USA) 00:51:14 I see it.
Kayla Reopelle 00:51:20 Oh, we got a… alright, I see, generated with local testing.
There's also… I don't know how relevant it is, to the way the instrumentation has evolved, or the operator has evolved, but we do have some unit tests for the New Relic one, that…
Might be helpful, might not be helpful, that you could look at if you wanted to add a little more testing.
Ariel @arielvalentin (ATX, USA) 00:51:46 To this thing, or to the operator?
Kayla Reopelle 00:51:48 This… to… to this thing.
Ariel @arielvalentin (ATX, USA) 00:51:50 It's jump.
Kayla Reopelle 00:51:51 Yeah. Yeah.
For the bundler require stuff.
Ariel @arielvalentin (ATX, USA) 00:52:01 Okay.
But what I'm gonna do is, Shawna.
I'm gonna do my best to try to review some of this this week.
I'll take a look at the demo video that you put out for the operator.
And see if we can try to get this published for you…
by next Tuesday, I wanna try to get this off of your plate.
It'd be fun to see it, like…
People not have to do anything.
For it to just work, right?
Xuan Cao 00:52:33 Yeah, but still, it's, it's kind of a, like, lambda layers that everything is,
So, so once you use it, you have a fixed version of, everything, so every time something changed, or, like, there's bug and we need to update, then there's, we have to update.
the operators.
Ariel @arielvalentin (ATX, USA) 00:52:55 I think we could probably set up, like, a…
like a GitHub action that will open up a PR using the observability bot in the…
Operator repo that does, like, a version bump.
Because the operator repo doesn't have… like, RenovateBot can't bump stuff, right?
In operators?
Xuan Cao 00:53:18 I think for the operators, they have this kind of stuff to keep tracking on, especially for the implementation of this kind of a gym, to determine if there's something new coming up.
Ariel @arielvalentin (ATX, USA) 00:53:31 Mmm.
Xuan Cao 00:53:31 I haven't looked at them for a long time. I don't know if they have it.
Yeah.
Ariel @arielvalentin (ATX, USA) 00:53:39 Oh, I see. So, let me just take a look real quick. So this is the Ruby Auto Extermentation.
So we have to find out from them whether or not, like, renovate that, we'll see…
Yeah, because I don't see anything that included update.
Right?
Everything here is in Go and YAML.
Xuan Cao 00:54:15 No, there's no such thing here. If you look at their, workflow, it probably has something, because, but, yeah, yeah.
Because this hasn't merged yet, so I don't want to break their CIs, they do something with it, so…
Ariel @arielvalentin (ATX, USA) 00:54:33 No, no, no, RZ.
Well, yeah, I guess, yeah, they have, like, dependency updates, and dependabot updates, and I don't know if they're using…
Like, a lot of this is Go. I mean, obviously, we can work with them to figure that out.
You know, like, if we have to put, like, a dummy gem file or something, or…
Or something to, like, force an update, but… I'm very clear.
Xuan Cao 00:55:09 Yeah, they… so… so they actually, so they are okay with, this approach, but they want to have, like, a one gem to install everything, instead of having, install, separately in, separately, so…
SSSY, that… that's why I…
We have to have this kind of dream.
to include everything.
they, they forced, JavaScript, did the same thing. Before, they have a… they… they… JavaScript had to install a lot of different, node package, and now they only just install one.
Ariel @arielvalentin (ATX, USA) 00:55:53 Wait, so, are you saying that they wouldn't let us install transitive dependencies?
Like, they wanted to be an all-in-one gem?
Xuan Cao 00:56:02 Yeah, they want to be all in one jam. Like, like, like, they want something kind of, like, instrumentation-all kind of jam? Yeah.
So, instead of installing Rails, adaptive action on upstream View, and they want to have, like, one solid, one consolidated GM to.
Increasing.
Ariel @arielvalentin (ATX, USA) 00:56:24 Yeah, yeah, I mean…
I totally get that, I just don't know, like… they're not gonna be… so, for example, like, okay.
Auto instrumentation gem, that's the gem that we install.
Xuan Cao 00:56:36 Yep.
Ariel @arielvalentin (ATX, USA) 00:56:37 But it has transitive dependencies, so it's gonna… it's going to have a runtime dependency on all
And all's gonna have its runtime dependencies on all these other gems, right?
So when you install the auto instrumentation gem, it's gonna pull down all the gems that it depends on.
Xuan Cao 00:56:54 Yes. Anyway, and that's okay.
Ariel @arielvalentin (ATX, USA) 00:56:56 Right? Yep.
So now we're talking about how do we keep the operator in sync with the auto instrumentation gem once it's released?
So, because I don't think Renovate bought… there's nothing in that PR that I saw for the operator.
That would… that would allow RenovateBot to say, oh, I need to update this Ruby Jam, because…
There's no gem file in there, or anything for it to look at.
Right? Wherever the auto-instrumentation gem is specified.
Like, I see source auto instrumentation, for example, there.
Oh, this is doing inline patching, and where's it getting the…
like, where does it install its gem from, by saying that, like, I require…
All… that's down here, right?
Yeah, where does the gem installations happen? I guess, once this is… where does the… how does Turntish and Ruby Gem get installed in this…
Dockerfile.
Can we scroll down a little bit?
Okay, these are… these are doing individual… so is this Dockerfile what is run?
by the operator?
Xuan Cao 00:58:28 Yeah, yeah, why… yeah, why don't try to build this, Docker,
container, although Docker image, it will run and stuff, yeah.
Ariel @arielvalentin (ATX, USA) 00:58:38 So it runs… so it'll have a container that's got the…
Auto instrumentation jamming it, or is this doing…
Well, because we haven't released it, this is doing individual.
Xuan Cao 00:58:49 Yeah, this is… this is old. That operator was at Jamie, sorry, the alternative stream of, how to, like.
Ariel @arielvalentin (ATX, USA) 00:58:59 Update this Docker.
Xuan Cao 00:59:00 file, basically. Yeah, I've updated this, this, PR.
Ariel @arielvalentin (ATX, USA) 00:59:04 Right. And because, like, Dependabot and RenovateBot can't look at this Dockerfile and say, oh, I see you're trying to do a gem install.
there's a new version of the auto-instrumentation gem out, I should bump the version in this Dockerfile.
Like, it doesn't do resolution of version dependencies in Dockerfiles, does it?
Kayla Reopelle 00:59:27 Don't think so, right?
Xuan Cao 00:59:29 No, no. Yeah, I think it was, I think I have a GEM file before.
you can look at it, but I don't know why I changed it to this.
Ariel @arielvalentin (ATX, USA) 00:59:42 Yeah, so if we had a gem file here, I think what'll happen is then the Pendabot or RenovateBot, we can register and say, run Ruby Updates. And when a new version of the auto instrumentation gem goes out, it can open up a PR and update
the auto-instrumentation gem in the… in the gem file.
Does that make sense, or am I barking up the wrong tree here?
You gotta get that? Sorry. Go on.
Xuan Cao 01:00:15 Yeah, I think, yeah, I'll… I'll…
try to use StreamFile again, but if there's anything that would block me to use DreamFile, I'll let so the team know that why it doesn't… you can't use Streamfile.
Ariel @arielvalentin (ATX, USA) 01:00:30 Okay, thank you for your patience, I appreciate it.
Kayla Reopelle 01:00:38 Right, that's our agenda. It's also time. Any last words before we all sign off for this week?
Okay, thanks everyone.
Ariel @arielvalentin (ATX, USA) 01:00:47 Happy New Year!
Kayla Reopelle 01:00:49 Happy New Year! Thanks for your engagement!
Xuan Cao 01:00:51 Thank you. Bye.
Kayla Reopelle 01:00:52 Week.
