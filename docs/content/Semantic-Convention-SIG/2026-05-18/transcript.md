SIG: Semantic Convention SIG
Date: 2026-05-18
Duration: 63 minutes
Zoom Recording URL: https://zoom.us/rec/share/iqqZAodsr0TMHGQg6ieNw9UvPwv6Xr1g6cudOzX00TLK0mXhHG35Flda4PyvO-Mn.92hLRB8G-9lf5HKj
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:04:20 Hi, everyone.
Ayushi Asthana 00:04:26 No.
Dhruv Ahuja 00:04:30 Hi, hello.
Liudmila Molkova 00:04:37 Okay, let me share my screen.
Feel free to add agenda items. Please add your name to the agendas, please.
And while we are waiting for people to join, let's do a little bit of a triage.
So, yeah, Pull requests that are ready to be merged.
C?
There were some open discussions… And it's in the same state.
So, for this one, we talked about… also stabilizing.
the entities.
Rotes… Take more time… Do we have anyone from the system semantic conventions here?
Doesn't seem so.
But… Let's add it to our agenda, and let's… See if we can have some additional… This question on this… Okay, hops thumb… Things that need more approval… I've had to… call with mainframe people last week, and they are interested in separating moving over to a new report for mainframes. So I think they are not going to really pursue merging this, but would rather Do it in their own repo.
Okay, there are a few more here.
I'm curious what's going on here.
I have some discussions, and I left a bunch of comments. Okay, they're resolved, I'll take another look.
Okay, block things… I think this… we wanted to move over to… the… New repo?
Yeah, I'm going to close it.
Great, and this one… Es… blocked… I think this is a part of the discussion of the process executable entity.
And what could be the identifying attribute for it?
But… It's essentially part of the SIG.
Review process.
Okay, we have a couple more minutes.
Let's take a look at entriaged.
Sorry, my cat wants to be around.
It learned it from you, Josh, from your cat.
Josh Suereth 00:09:24 Yeah, it's funny how they learn from each other.
Liudmila Molkova 00:09:26 Yeah.
Okay, pack version using Renovate.
Oh, wow.
That, that, that, that's fun.
I think Trasky left some comments before.
Are you interested in this?
Trask Stalnaker 00:10:12 I can take a look. Is this something… Oh, yeah, I think I did this for the Gen AI… SEMCOM repo, because Josh had made… left that comment earlier about using Renovate to update from the core semantic convention.
So, yeah, I can take a look.
Liudmila Molkova 00:10:38 Thank you.
Let's see what else… This is awaiting Cardano's approval.
This is also probably of 18 codoners approval.
Yeah.
Oh.
Some of the Kubernetes attributes go stable.
And there is a SIG approval.
Wow.
Time to celebrate!
Trask Stalnaker 00:11:19 Yeah.
Liudmila Molkova 00:11:24 Okay.
Cool, so then we are at the end of our triage window. If we have time, maybe we can… Look at more things after.
And… what do we have on the agenda?
the risk.
Do you want to talk about it? Do you want to present, or… present.
Trask Stalnaker 00:11:53 Yeah, we can just, if you want to go back to the meeting doc, I think going through that thread will probably be more confusing than just explaining here. So we have, in GenEI, we have a histogram For token usage.
I think it's problematic, but I would like to bring the reasons here and get, kind of, some general SEMCON guidance.
The reason I think it's problematic is that it is a histogram But it has an attribute which splits the value.
So you've got number of input tokens and number of output tokens.
And… I… I looked, I did not find any other… Histograms in semantic conventions which do this.
The problem comes because if you aggregate away Token… the token type attribute.
You might think, okay, now I'm getting my… total tokens.
But you're not.
The count, or the sum of the histogram, yes, will be the total, but the histogram values will be distributions across input tokens and output tokens. It won't be your distribution of total tokens.
Josh Suereth 00:13:40 So, quick question, they're separate time series, though, right? Because of the attribute? So the only way the count would be wrong is if you aggregate across all the attributes.
Trask Stalnaker 00:13:52 Right, right. So if you fill… if you take out… If you, say, define a metric, do you… That removes the token type attribute.
Now, you've changed… the… The distribution is not your… the sum is total tokens, but your distribution values are not total tokens.
Josh Suereth 00:14:19 I don't… that… this doesn't make sense. Like, why… why would that happen?
like, we compute the sum and the buckets and everything independently per metric stream. So the attributes are different, you get a different histogram.
So the only way you're going to end up with things bucketed together is if you aggregate away that label.
Like, I'm not saying that it's not weird, but the thing you're describing, I don't understand how that could be happening, unless your metric system is not behaving correctly. Like, I don't see that happening in Prometheus, I don't see that happening in, like, our metric system.
Right.
And, like, in the.
Trask Stalnaker 00:14:54 Sorry, you'll have to slow down for me. Yeah.
So, tell me what, what you're thinking is happening.
Josh Suereth 00:15:02 So, so when you make the histogram, right, you have an attribute which is token type.
Token type is either input or output.
So you end up with two histograms, one for input and one for output.
Trask Stalnaker 00:15:14 Right.
Josh Suereth 00:15:15 Inside of that input histogram, the.
Trask Stalnaker 00:15:17 Well, you end up with two time series in the histogram.
Josh Suereth 00:15:20 Yeah, you have two time series. In the one histogram for input, the count will be the tokens that came in.
And in the time series for output, the count will be the tokens that went out. The buckets will be the same.
Now, if I aggregate away that metric, I created something which is meaningless.
Trask Stalnaker 00:15:36 Right? Yeah.
Yes.
Josh Suereth 00:15:38 That I agree with, yeah, yeah. Okay. So it's basically if you aggregate away, but if I aggregate away, my input and output tokens would add together.
In some weird way. So I'm still adding things, like, in the data model. It's just…
Trask Stalnaker 00:15:51 Really stupid.
Josh Suereth 00:15:52 it weird.
Trask Stalnaker 00:15:55 The values, though, that you're recording, your histogram buckets, are not going to be… you're not going to get, like, 95th percentile of total tokens. You're gonna get 95th percentile of the union of input and output tokens.
Josh Suereth 00:16:13 Right.
But… Okay.
Michele Mancioppi 00:16:20 Yeah. I mean…
Trask Stalnaker 00:16:22 Which is nonsense. I agree. I agree with that part. It's not… it doesn't make sense, and that… that's why I think that… We've modeled it incorrectly because we've set up a case where Common usage is going to provide Nonsense.
Michele Mancioppi 00:16:41 Yeah, I see it a lot with, with end users.
If you model metrics so that an aggregation is required for it to make sense.
90% of the people will not get it.
So having to set a filter, like, type output or input.
nobody will understand. We shouldn't do that.
Trask Stalnaker 00:17:11 Christoph?
Christophe Kamphaus 00:17:13 I have two points. One is a question.
What do the buckets represent?
Trask Stalnaker 00:17:26 That's a good… Related point.
But the buckets… represent… the union of… Input and output tokens.
Michele Mancioppi 00:17:41 I think the question is, like, each data point, is it token per message, token per session, token per…
Trask Stalnaker 00:17:49 Token per message. So each, yes, each inference call, for example, what are my input tokens, and what are my output tokens?
Christophe Kamphaus 00:18:02 Okay, so you could, through that histogram C, The distribution of tokens per message.
Trask Stalnaker 00:18:12 Not distribution of total tokens per message.
Because if, say, total tokens is 100, And… you're recording two different histogram values here, the way it's modeled today. If it's, say, 80 and 20, 80 output, 20 input, 20 input.
80 input, 20 output.
You're going to get, Those two values in your histogram.
80 and 20.
Christophe Kamphaus 00:18:49 Okay, no, I get it.
And my other point was… I think in CICD, we had a similar issue with Pipeline duration histograms.
So… If I remember right, we switched there to use gauges.
Michele Mancioppi 00:19:16 But… How would it… Makes sense in this case. Does the… The gauge shows you the sum of tokens in the time period.
Trask Stalnaker 00:19:28 No, but at least you're being honest that gauges don't aggregate.
Josh Suereth 00:19:33 Right, right, but sums do aggregate. So, I guess the question is, what are you trying to measure, right? And is the merge algorithm working on your behalf? Like, the question we should always ask with metrics is, is the default merge the thing we want for most people?
And then what… how is the usage of the metric? So basically, anytime you do a counter, you're effectively doing a rate. Anytime you do a histogram, you're doing a rate plus percentiles.
Right? In this case, your default percentile algorithm is not at all what you want, because you're doing the percentile of, like, the union of inputs and outputs, and that's just weird, where you want the percentile of the total token usage for a task.
So, like, I… I… that…
Liudmila Molkova 00:20:17 No, no, not, not really.
This metric is a proxy to cost.
And people want to see number of input cache, read tokens, input cache, write tokens, output tokens, reasoning tokens, all independently, because they multiplied by cost of token for this thing.
And this list is going to grow, by the way.
Right.
Trask Stalnaker 00:20:44 Then it… should it be a counter?
Josh Suereth 00:20:47 Yeah, if it's a counter, then you aggregate totally fine.
Liudmila Molkova 00:20:51 If it cuts to…
Josh Suereth 00:20:52 It's because you're trying to get, like, 90th percentiles and 99th percentiles.
And then it doesn't aggregate, you'd want to have a different metric name.
Liudmila Molkova 00:21:00 So for costs, purely.
Counter is fine.
The histogram may still be necessary for the distribution, but that's probably of less of a value. We can probably drop it.
Trask Stalnaker 00:21:19 Brought up a good point in the discussion thread that, the… There is value in that, The… having distribu… having distribution of the total count being how close are you… the sum is how close you are to the complete… the, what, the window, the context window max?
I think is input plus output.
Liudmila Molkova 00:21:48 Oh, and then we would measure the size of the context window in session.
It's, like, different metric than.
Trask Stalnaker 00:21:57 Yeah, but it would be… I mean, it could be interesting to see, oh, 90… my… I have… You know, how many requests are in the 95th percentile of… Sorry, I've got lost. Go ahead, Josh.
Josh Suereth 00:22:16 Yeah, I mean, so fundamentally, every histogram can degrade… can degrade to a counter.
Right?
Which I think is why it's, like, natural for you to try to force-fit this into a counter and make histograms work, but histogram aggregation is complicated in ways that confuse people all the time.
It's incredibly useful, and it's really efficient when you want to get, you know, percentiles.
But… Yeah, I guess, is our percentiles I, you know, again, I think we should tie this back to use case. If you know what the use case of this metric is, and primarily how people are going to be interacting with it.
I would tie your metric type to the use case and make sure that it's easiest to solve that use case, but I would also suggest it's possible you have more than one metric for the different use cases, and some of… like, maybe the histograms are optional and the counters are always on.
Because you're gonna hit more use cases and scalability that way, right? But, like, unless you need the percentile, I wouldn't use a histogram, I'd use the counter. So, unless the percentile is, like, super critical to your use case.
Trask Stalnaker 00:23:35 Cool, that… that helps. Yeah, I mean, I thought this was really interesting because I hadn't run… I went back in the history of, and of the creation of this, and I think part of the reasoning was, histograms.
Are the… like, a counter can always be… turned… it can be made a histogram, and you don't lose anything, you only gain something. And I would have said… I would… I thought that as well, until this kind of weird case came up, of splitting a value there.
Michele Mancioppi 00:24:12 But, so, do I understand correctly that the idea is… What's the shape of the metric now?
Trask Stalnaker 00:24:20 It's a histogram right now, with one required attribute.
To split it by input and output.
But there's a proposal… the reason why this came up recently is there's a proposal to split it further by, cached… Tokens, and by reasoning tokens.
Michele Mancioppi 00:24:44 Yeah, but then, I… honestly, I believe this stuff should be in the metric name.
to lift.
Trask Stalnaker 00:24:52 If it's a histogram.
Michele Mancioppi 00:24:54 Yeah, then to lift it up, yeah. If it's a histogram, lift it up, because people are gonna get mighty confused.
It's like if we got rid of the server and client part of the name in HTTP metrics, who's gonna understand that?
Liudmila Molkova 00:25:09 And then this list of metrics is going to grow endlessly.
If it's part of the name, because providers give more and more breakdown within their, number of tokens.
Trask Stalnaker 00:25:25 Yeah, I like the idea of just… of converting it to a counter, because we can… it can grow and grow within that counter.
And then, based on… Use case… We could add… additional metric.
hist… Of histogram… Type.
If people have a particular… Need, like, for that.
Liudmila Molkova 00:25:56 And you would add another attribute that's the subtype, or… would we… I was thinking that one of the ways to solve it The other problem is that we have a type that's more granular, so it's input, cache, write, input, cache, write. It looks ugly as hell.
But it's one of the options.
Trask Stalnaker 00:26:19 Yeah. Yeah, I'm not sure how I would… I'm still not sure how I want to solve that PR problem.
I just… Wanted to first… Get this piece out of the way.
Cool. Thank you all.
Liudmila Molkova 00:26:41 Thank you.
Okay, moving on, Ayushi, is this how I pronounce your name?
Ayushi Asthana 00:26:52 That is correct.
Liudmila Molkova 00:26:55 Thank you. Do you want to present? Do you want me to present?
Ayushi Asthana 00:26:59 I think you can open the pull request that has enough context. If you want to dive deeper, I can present the doc.
Liudmila Molkova 00:27:10 That would be wonderful, actually.
I think we talked about this in the past, and sorry for not taking any… not providing any feedback, but I think most people here have context, maybe if you can spend a couple of minutes refreshing.
It would be great. But I can also… I would love you to present the doc.
Ayushi Asthana 00:27:34 Yeah, I think I'll then present the doc, and I'll give a short summary.
Liudmila Molkova 00:27:39 Sounds great, let me stop sharing.
Ayushi Asthana 00:27:44 Oh, okay.
Cool.
Right, so, I think the PR that we just saw adds data as an attribute group under the purview of Service and Deployment SIG.
And I believe the question was, why are we adding it to the service and deployment SIG?
And I've added some commentary on why that makes sense, but basically, because we are dealing with the cargo that is handled by services, and There, there is… there is some cohesive, semantic of Services and data and deployments together, deciding the security attributes for a specific request or security and governance decisions, which is why I had proposed that data as an attribute group should come under the purview of service and deployment.
Some of the use cases that we had discussed earlier for data as an attribute were data category and data sensitivity, which will be attached to requests, spans, metrics, or logs.
By specific, services, or by specific applications.
Where they can define Whether they are dealing with requests that should be labeled with a specific type of sensitivity, or with a specific type of category.
These values are examples at this point. We have not decided on whether this should be enum or open.
But because of the fact that services can attach these attributes to requests and logs, and because services can have multiple data sources, and it could… like, data… data is not going to be like, an entity or a data store. It's hard to model it that way as an entity, so we had kept it closer to services and deployments so that we can define some of these things, some of these semantics.
So… That was the rationale going forward, but I would like to hear questions or concerns or suggestions from the group.
I'll… I'll pause. If… if you guys want me to expand on any of the things that have… that I've written on the doc, I'll do so.
Liudmila Molkova 00:30:24 Yeah, I think what we discussed in the past is that Duh.
The scenarios are super interesting.
the data… The root namespace data is very, broad.
It could mean anything, and when you attach let's say, data sensitivity to an HTTP server request, it's not… always clear what it means. If it's per request, and there is special instrumentation, then it kind of makes sense.
the… I think that the plan we discussed, that maybe we can think about, Different name that's less ambiguous.
Or maybe if we can… Pretend… the data with something like service data, if it's a resource attribute.
So, if you are, attaching metadata to, to, the entity or resource, then it, it's… It's clear. The scenarios that are… where this flows through the system, and it's dynamically attached to telemetry, those are a little bit more, unclear.
So maybe you can guide us through those?
Ayushi Asthana 00:31:57 I think I can talk about some of the demo scenarios that I've added. I hear your concern, but I feel like having it as a resource attribute, like, the whole idea of proposing it as an attribute group was that, that meaning can be dynamic, so it's possible For, data sources, like buckets or databases, to also broadcast that… A certain type of sensitivity.
And it's also possible for services to do the same thing while they're handling some PIIs, right? So, these were two demo scenarios that I had added. I think the requests are closed at this point, but basically, what had happened was, I had added a demo where, for certain payment gateways, or for payment services, basically, we configure that entire service to have data sensitivity high, because it's a payments service handling, payments data.
And so, based on this, you could configure your collector to redact all logs that are coming out of the service, right? And in this scenario, the service is defining that the data sensitivity for for my case is high, and so I want collector to behave a certain way when dealing with the telemetry that I am, sort of, So… publishing.
The second one for category was similar.
slightly similar, I'd say, I don't know. But basically, this was where we were saying that there is a service that is handling one service, multiple services, that are handling different types of data sources, and now this data category could be based on data sources.
And we could say that, okay, I am handling different requests that are going to deal with different data sources, and this is also very service-specific, by the way. For the use case that, basically we are talking about, where a specific attribute is propagated through a data source and into the request through context baggage. I think I don't have a working demo for it at this point, but… I had proposed pseudocode for it, all your… I believe… Right. I think this is the one that you're referring to, where… Basically, we set… The context baggage when we are reading from a specific data source.
So… while I understand why we might want to do it, this is, as an attribute, is supposed to be more dynamic.
In the sense that, you know, services could have their own Sensitivity while they're reading from multiple sources.
So it's not going to be attached to a single entity at any point, or be, like, very… decisive.
Liudmila Molkova 00:35:12 Yeah, I think the two important distinctions are… oh, Trask, sorry, you had… you have your hands up.
Trask Stalnaker 00:35:19 Continue. Go ahead and finish.
Liudmila Molkova 00:35:21 Yeah, so my, my, my point was that there are two main… from modeling perspective, two main use cases. The first one is resource attribute, the second one is panorametric attribute.
And the first one should probably be fine with service prefix, the other one, this is the interesting, and this is your use case, too.
It seems. I'd like to talk more about it, but I trust… go ahead.
Trask Stalnaker 00:35:48 I'm… do… the… the connection I see for the question of whether it could be a resource attribute is… Mmm… In my mind, it was more about trying to find a home for this data.
Namespace.
And so, if there wasn't this use case.
Like, it feels like kind of the main use case is probably that it's service, Specific?
Then that would be a good home for it.
But if the… if it is an important use case to… Cover, you know, this dynamic, use case.
I think we still have the question of what is the namespace.
data, it could work, but it would be a major commitment.
I feel like, for… to… Be like, that this is so important that, you know, this data, we'd really be leaning into, like, such a potentially broad Namespace… For… doing this.
I… Have you… do you have any alternative options for top-level namespace, like… I mean, like, sensitivity as a top-level namespace, something that, you know, gives us that Description of, you know, why… We're interested in this namespace, how it differentiates from all the other namespaces, all the other potential use cases.
Ayushi Asthana 00:37:37 Okay, if I understand the question correctly, why do we want to introduce data as a separate attribute group, and not use… Other top-level namespaces that we already have to satisfy these use cases, right?
Trask Stalnaker 00:37:55 Not a… it doesn't have to be an existing namespace, it could be a new namespace, but something that… Is a little bit narrower.
That… Yeah.
Ayushi Asthana 00:38:10 Okay, bye.
Say.
I don't have, like, any options off the top of my head at this point, because when we thought about this.
earlier, the idea was that we would like something that would tell us what is being processed by a specific pipeline, whether it be network, or application, or a short-running process. What is this Basically container processing.
And what is the, sensitivity or category of the data that is… it's trying to process. We had debated data source.
But then, when we moved from entities to an attribute group, where we were, sort of zeroing in on, that we want to deal only with cargo, and it's okay if a data source is able to tell us sensitivity, but this is not the intent. This only deals with what is the service or application, handling, basically, right? So, that is where data as an attribute group came up.
I'm open to suggestions. I can go back and… go back to the drawing board and think more about this, but data seemed like the right thing to handle, at least A few of these use cases where we handle what is being processed, and what do we know about the thing that's being processed by, this entity?
Right?
So that was the main idea of choosing data as the attribute group.
Trask Stalnaker 00:39:56 Yeah, I mean, I agree that data fits this use case.
My worry is that data fits a lot of other use cases as well.
Ayushi Asthana 00:40:08 Right, so… I, I…
Trask Stalnaker 00:40:13 But I'm… but back to my… yeah, the first thing I mentioned, though, is… I mean, I could still see data working.
for this.
But again, it's a much bigger commitment from… Our… from semantic conventions to be like, yes, this is, you know, we're leaning into this data namespace, this is what it means. It just… it's justified the possible, you know, confusion of other people wanting to put other, you know, kind of narrowing what data means for semantic conventions.
Ayushi Asthana 00:40:52 Right. That… that makes sense. I think that's a valid concern, to be fair.
I think we can do this, right? One is have a narrower definition, maybe try to make it more well-defined.
And the other thing that I can think of is… Should we have more use cases over here, where we think that data as an attribute group would serve well, so that Basically, I think more attributes that seem like a good use case for data would also help Lead to a more well-defined, Group, basically, right?
Trask Stalnaker 00:41:43 Yeah, that could help us give, like, the bigger picture of, kind of, forward-looking of what kind of… I mean, we wouldn't want to define more attributes in this namespace now, but it could help us to… You know, make sure that this namespace is on the right, you know, long-term path.
Ayushi Asthana 00:42:03 Right?
Josh Suereth 00:42:03 I wanna… wanna jump in with two things that I wanna say, if that's okay. One… one I think, helps with the current discussion, one is just something you said, Jess. I don't want a sensitivity namespace to have… to be this use case.
Predominantly because I think we probably need to annotate every attribute we have with sensitivity level, and have a notion of, like, what to automatically redact, and I'm worried… this use case is a little too tied to data.
and not enough about just general sensitivity handling. So, like, yes, it allows you to redact things, but it'd be like, when the data sensitivity is this, I redact sensitive attributes, and I want to be really careful about how we… think about that. I think that, like, again.
to your concern about, like, data being broad, I think sensitivity is really broad in the same way. So, I think we're in a world where we're gonna have broad attributes no matter what. So, I think we have three paths forward, right? One is, what's proposed here, we could say, you know what, we think this justifies a data group.
But we are going to explicitly allow this use case and no other use cases without some formal proposal, and just put that in under the data thing of, do not add to this group without making a proposal around your use case, something like that, so that we aren't opening the can of worms immediately.
And people know that there's a high bar of entry, right?
Option number two is we, We look for another alternative, right?
So, we try to find some kind of a name that somehow toes the line of not opening a can of worms, but being very tied to this use case. And I… I'm a little bit nervous about that bike shedding, but I think that that's an option of something we could do for number two. And then the third thing would be, we could go with, actually formalizing sensitivity overall, and make this, like, a whole formal giant proposal.
I'm a little bit nervous about that, because I think, again, we know how these things go, right? Like, I agree with you, this is a commitment, and this is a thing that we're trying to make progress on, so I see option one as.
what's the minimum we can do to make progress without fully committing to everything? Option two would be, we're scared of number one.
So we're trying to make a workaround, but I… that doesn't make me happy. And option 3 is, we're just gonna eat the whole enchilada right now.
I feel like we need to pick one of those three, and obviously with what I just said, you can see where my bias is.
Liudmila Molkova 00:44:34 On… I think I have an option on how to… Limit the blast radius is… We know the service data sensitivity looks good, or service criticality looks good, or the resource level attribute looks good.
the smaller scope could look like, okay, if we do the dynamic thing, can we… PrepEND.
The… that there is a pattern of data or something.
But depending on the scenario, depending on the service, we prepend it with something That makes sense for that case.
My worry about data is that data.
it's hard to understand what data means in the context of HTTP requests. It's actually not a property of the request, it's a property of this operation, transaction, or something.
And then it becomes, I don't know, transaction data criticality.
So this is the other option of making it smaller.
Ayushi Asthana 00:45:57 Maybe I'll take that into consideration. I'm not… Entirely sure how that'll be modeled.
Immediately.
But I'll take that into consideration.
Bye.
Liudmila Molkova 00:46:36 Maybe… So I think, to the… option I've provided. It actually depends on the… How you are going to use it, whether you depend on Evan… Specific attribute, meaning… Like, they… that you query by. So… It's probably in your document, but maybe you can… talk a little bit about the… the consumption of this data. What… What are the specific scenarios where this data helps.
Ayushi Asthana 00:47:21 Great.
I think, yes, we can talk about that. So, currently, there are use cases in different providers, That, that… in some way or the other, try to, label sensitivity, or try to label category, right?
So, for example, for Datadog, right, they have A sensitive data scanner.
That can be configured on certain types of regex matching, and it's able to redact logs based on, that matching, right? I believe That is a use case for this data scanner, and this maps directly to data sensitivity, where It can, sort of… interpret high sensitivity as complete redaction, and it can have rules around data sensitivity high. Similarly, they have routing that is specifically meant for Routing high-compliance data to different types of storage versions or storage locations.
And that maps to a data category where they can use data category to do such type of routing, right?
And most cloud providers have similar use cases for sensitivity and category. Splunk has a use case of where it tags different types of, Security findings based on, yeah, it tags, basically, security findings.
And… Based on the sensitivity label of data stores, and that also directly maps to what we are proposing at this point.
Da-da-da!
Splunk also has something called a service maps at this point, and I could see Service Maps using data category as a field, so this is what, like, a basic service map looks like for Splunk, and I believe Data category could be a good field for this service map, showing what services are handling what type of data in this map, right? So this is another use case that's possible with data category.
I think I've listed a few others over here.
Oh.
Liudmila Molkova 00:49:57 Essentially, those are the security use cases.
Ayushi Asthana 00:50:01 Yeah. This one, I think the service map thing is not a security use case that we're doing with data category, right? This is more of an observability thing that you can do, where you can trace what all services, how a specific type of data is flowing through your application.
And create… if you would like, create network boundaries around it.
But, yeah. Mainly, there are security use cases or compliance use cases with data sensitivity and data category.
Liudmila Molkova 00:50:35 Yeah, and help me understand, so this is the… Regardless of the scenario, whether it's a resource attribute or it flows with the request, It's the user application.
Populating this information somewhere.
the baggage, or in the resource attributes, and then there is the consumer, which filters based on this data. Does… what?
Why, why do you want to… have one attribute. How does it help? What depends on it being standardized?
Ayushi Asthana 00:51:16 I think… The main thing is that across providers, right, this is being done in different ways.
And what helps with this being standardized is, we have a singular definition of what this cargo means. The logs… the data that's being handled by the service.
What are the attributes of this data that my service is processing? Is this sensitive data? Is this personal information? Is this financial data? And what do I want my observability metrics, or my observability providers, or my dashboarding to do based on this information that I'm providing them.
So if… if this is, for example.
PII. Do I want my observability providers or my collectors to be handling this data differently, the metrics that I'm exporting? Do I want these metrics to be under lock and key?
Basically, providing storage access to only certain admin groups and not everybody. What do I want to do with them, right? And this will be a standardized way to say, hey.
this data is sensitive, I want you to handle it a certain way, and this is the way I say that this data is sensitive for everybody, right? So that is… that is the intent, that I'm able to tell across the board that this is the data I'm handling, and this is what I want you to do with the sensitivity.
Liudmila Molkova 00:52:49 I see, so this is for the consumers. We want to have either reusable pieces on the consumers, or different consumers doing the same thing based on those attributes.
Ayushi Asthana 00:53:02 Right.
I think I have listed down what, different providers produce.
In terms of sensitivity, and in terms of category on their side, and what is missing at this point.
So, folks can, like, look through what currently happens.
And what will be consolidated in case data becomes an attribute group, and so this behavior is going to be uniform across both publishers and consumers.
Liudmila Molkova 00:53:44 And I would imagine, you're representing the GCP part of the consumer.
Ayushi Asthana 00:53:50 This is…
Liudmila Molkova 00:53:51 What you would, the solution that would work for GCP, is it the case?
Ayushi Asthana 00:53:58 I don't think this is, the specific use case for, these two things is limited to GCP, because, across providers, we're doing cataloging in some way or the other, right? We have AWS doing data cataloging, like, Azure doing data cataloging.
Oh.
So… All of them are producing data categories or data tags in some way or the other, and this unifies the experience on what… once the data… once the telemetry comes out of providers, what does it look like? It's… it's a singular data.category, or data.sensitivity. It's… it's uniform across the board.
Same for, I think, Kubernetes. Kubernetes does not have, like, a singular way of defining either of these things.
While it could do that.
Once we have these attributes in place.
Still on this floor a little bit, but yeah.
Okay.
Any?
Other questions at this point?
Liudmila Molkova 00:55:26 So my… I'm going to share my main concern with the… the… the… the… approach is that Annotating this whole span.
was… Data sensitivity is very limited because you cannot… The… the… you can redirect the logs, or you can… Redact them.
But the next step would immediately be that Only certain parts need to be redacted, or only certain things need to be… redirected.
And… I feel like it's important, and it solves some problem, but it doesn't… doesn't solve… The more granular.
Bing.
Ayushi Asthana 00:56:23 Agreed, yes. I think, I think to that, Josh's point was valid, where, we have sensitivity as an attribute for, Most major, resource entities And we're able to say, in the configurations, exactly what we want redacted. Do we want only high sensitivity things redacted, or do we want everything redacted? So, if you look at, Basically, here, right? Here, I've set the whole body to be redacted, but it could be something else. It could be based on regex, it could be based on, like.
It could be a custom configuration, basically, is what I'm trying to say. It doesn't have to be… right now, we're just introducing an attribute.
How this attribute is handled by different collectors.
could be different behaviors based on what is required at that point. But the main idea is to be able to tag a specific span, log, or metric a certain way. What we do with it later is… Configurable, even at this point.
So for example, you could, you could say something like this, right?
Liudmila Molkova 00:57:52 Kristen?
Ayushi Asthana 00:57:53 Does that, does that answer your question?
Christophe Kamphaus 00:57:57 if I followed the concerns right.
Then, the problem was just marking the whole span, or… Log event as sensitive.
Is that, you cannot be granular. You cannot just… If you want to have only certain attributes redacted.
You cannot distinguish it, or if you want to have Certain logs handled in one way, and other logs you might want to redact other attributes, you cannot specify just with a sensitivity label. Is that what you… Wanted to say.
Liudmila Molkova 00:58:39 Yeah, that… that… Thank you for… Expressing it better.
Ayushi Asthana 00:58:47 Yeah.
Liudmila Molkova 00:58:51 So I would be interested in finding some less ambiguous namespace, and I think that's the only, problem. Like, the small… prefix that makes it more specific would solve all problems for me, because it gives us ability to experiment with it. It feels like we need to experiment a lot, because we don't know what consumers will do, if it will be generically useful for all of them.
Everybody would write their collector pipelines in a certain way, and to a certain extent, it doesn't even… Help a lot to standardize.
The set of attributes, because it's all very custom for now.
And if we have some namespace to experiment, In?
It would be a very… A low risk.
Change.
Ayushi Asthana 00:59:46 Seth?
Okay.
I think… duly noted.
I can… Brainstorm on that a little bit more and come back.
To the sake.
with… either a more solid definition or a more narrow namespace. I think we can do that.
Liudmila Molkova 01:00:14 Yeah, thank you.
The sheet of the details.
Okay, I think we have just one more item on the agenda, and it's the… R… process entities, and we don't have anybody from the… the system SIG here, So I wanted to check what people think.
So the context… Some of the process attributes go to RC.
It's not a problem, but entities that don't go to RC as well, and Braden is saying that it will take A bit more time.
2… RC entities.
I'm thinking it's… it should be okay to let this PR go, but, require… Entities… To stabilize at the same time as attributes.
How would people feel about it?
Here.
Yeah, Josh?
Josh Suereth 01:01:28 Yeah, I think it's fine to… like, I don't think we're gonna change the definition of process bid, so I think it's fine for that to remain. They might change the entity definition of, like, what's identifying and not, so I think that's fine. You know, my only concern is if we're stabilizing Like, all of the host metrics and things, and we change the identifying attributes.
On the metrics, that's where things get awkward.
Right? Of, like, what… because that changes the time series, but that's not what they're doing here. They're just actually taking some of the attributes where we're not going to change the definitions. So, I'm… I'm actually fine mer… like, thinking through all of it, thinking through where they are. I think this is fine as an exception.
Liudmila Molkova 01:02:12 And also what you're saying, that event stabilization would be fine without entities.
Because that… this is our seat, this is… does not.
Josh Suereth 01:02:19 This is our… I think stabilizing the attributes is fine with NRCs. Where I would draw the line is actually the… if we try to stabilize the metrics, and we aren't… because these are the first set of metrics where the entities matter a lot.
If you look at the way process metrics are defined, the entity carries the heavy weight of, like, what the identity of that metric will be.
So, that, that would be my concern here.
I wouldn't let the process attributes go stable without, like, the entity identity being stable as well.
Liudmila Molkova 01:02:54 the practice metrics.
Josh Suereth 01:02:56 Sorry, yeah, process metrics. Yeah, process… I keep misspeaking, my bad. Yes, the process metrics, the actual signal itself. But, like, we should stabilize the attributes, because I don't think we're going to change the name of it.
Or the meaning of the name.
Liudmila Molkova 01:03:13 Any concerns from other people, Uber?
Oh, okay, cool.
I'll capture it here, and we are one minute… Away from our… Painbox, so I'm going to call it… Thank you all. Great discussion. See you next time.
Trask Stalnaker 01:03:34 Bye.
