SIG: LLM Semantic Convention WG
Date: 2026-06-05
Duration: 114 minutes
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:00:18 Oh, hi, Jamie!
See me here.
Jamie Danielson 00:00:21 Hi, I just… I just happened to open CNCF Slack and saw this, and I'm like, good timing, I didn't miss it.
Liudmila Molkova 00:00:29 Nice.
Jamie Danielson 00:00:31 But that means I didn't come fully prepared, so I figured I'd at least just listen in.
Trask Stalnaker 00:00:36 I didn't do my homework either.
But I did write the PR, so the information is back there somewhere.
Jamie Danielson 00:00:45 Yeah, you're in a much better state than I am right now, which is why I'm here to listen.
Trask Stalnaker 00:00:55 Hey, Aaron.
Hey, Alex!
Golgi Apparatus (us-cam-5cc) 00:01:04 Good to see you, Alex. It's been a while.
Alex Hall 00:01:06 Yes.
Trask Stalnaker 00:01:09 Yeah, thanks for joining.
I can drive this… Boat… Let's see, so we wanted to talk… Through… things in this PR, so tokens. Tokens, tokens, tokens.
Okay.
I did see… Alex, you had some recent comments… Why don't we start with… your recent comments, and then we can kind of go from there, because I think those… Brought up some… some… kind of… fundamental-ish questions.
Yes.
They are confusing.
Actually, this was interesting… Dean, I hadn't thought about this factor here, because one of the things I was… trying to do was I was trying to… I had this in mind, that we… the metric would be… could be used for cost.
calculation… And so that drove some of my modeling.
Maybe it can still be a proxy.
But let's talk about what, so you're… Suggesting here all potentially just a large number of simple counters, as opposed to trying to Split it dimensionally.
Alex Hall 00:03:18 Or even Instagrams again.
Liudmila Molkova 00:03:25 Look for the… Every attribute we're introducing broken down by modality, input, and fashion would have a metric.
Alex Hall 00:03:34 I didn't catch that, something funky.
Trask Stalnaker 00:03:36 your… Yeah, your audio's a little… Garbled.
Liudmila Molkova 00:03:41 is it better now?
Trask Stalnaker 00:03:46 Yeah.
Liudmila Molkova 00:03:47 Awesome. So… for each… Modality… input, output, and cache status, we would have a metric. Like, whatever… For each attribute, essentially.
Alex Hall 00:04:03 more than that, really. It wouldn't be, like, every combination only, it would also be subsets, so you'd have different levels of granularity at the same time. They would overlap.
In the same way that the span attributes do.
Liudmila Molkova 00:04:22 Okay, so also the… Total input tokens, total output tokens. Total.
Cash tokens, regardless of modality.
Alex Hall 00:04:33 Dental image tokens, regardless of cash.
Maybe even total tokens.
Liudmila Molkova 00:04:44 I kinda like the idea of… Input and output tokens.
In addition to breakdown, like… The higher level view, so people don't… Need to query all those different metrics and then aggregate them on their own.
Trask Stalnaker 00:05:12 So, what would that… We would, input tokens, output tokens.
Would you still have a… You still have a… By cache, by phase, or that would be, like, read…
Alex Hall 00:05:35 I think there wouldn't be any… attributes… corresponding to cache or modality.
There would still be attributes for, like, model.
But potentially, the metric names could be exactly the same as the span attribute names.
Which would at least be very simple to explain.
and implement.
Liudmila Molkova 00:06:10 And so, like, this per-attribute metrics would be… Histograms, but aggregates of them, like input-output, would be counters, because histograms don't work well there as That's what I think we're trying to solve, partially.
Golgi Apparatus (us-cam-5cc) 00:06:29 So, I understood for, like, input-output, it totally makes sense to not have them together, but, For the other ones, can someone just give me a refresher on… What's wrong with having them in a single histogram.
Like, I get the general idea, but… We also have This kind of issue with, like, database metrics where, for example, different tables Would still roll up to the same metric, right?
Trask Stalnaker 00:07:07 I mean, database t- I'm not sure that's the… Best analogy, because of the multiple dimensions… Here… Where, like, database… Span, there's only one attribute table.
That's… I guess there's other attributes, but… there's other attributes, but they're… I don't know, tokens is… Confusing, because it's… Pieces of, like, their… They're subsets of each other in weird ways.
Golgi Apparatus (us-cam-5cc) 00:07:53 But, like, the… yeah, I agree on the subsetting thing. I guess I just didn't understand for… besides input and output.
Whereas, like, the overlapping… Happening.
Like, for…
Liudmila Molkova 00:08:09 The cache is part of input, right?
Golgi Apparatus (us-cam-5cc) 00:08:13 Did… did…
Liudmila Molkova 00:08:14 The medallion.
Golgi Apparatus (us-cam-5cc) 00:08:16 Sorry.
Liudmila Molkova 00:08:20 No, I'll finish your thought.
Golgi Apparatus (us-cam-5cc) 00:08:22 Sorry. I was gonna say, do the LLM APIs all return Cash.
Sorry, input tokens, including the total… Cache input tokens, or does it partition them in the response for you?
Trask Stalnaker 00:08:41 I did.
Berries is part of the problem we're facing here.
Is that, sometimes… It is… and there's some other weird overlaps that… sorry, I did not refresh myself on this.
All the nuances here.
Liudmila Molkova 00:09:10 So, like… Some providers would give you the number of input tokens total.
And then in the details, there will be a breakdown by modality, And cash.
And sometimes they want to give you the breakdown, or not enough breakdown.
Golgi Apparatus (us-cam-5cc) 00:09:34 Okay.
Liudmila Molkova 00:09:35 Save as output.
Reasoning as part Of the output, but sometimes you don't know. I think Entropic does not return.
Number of reasoning topics… oh, sorry, tokens but returns, the total output tokens.
Golgi Apparatus (us-cam-5cc) 00:09:52 Okay.
But I think… I think I'm on the same page with that. And the only other thing I was still not sure on the premise of was, how does the counter help? It sounds like maybe we're not on that solution anymore, we're back to Instagram.
Trask Stalnaker 00:10:13 I think… Let's… I mean, let's address that.
Separately… Of whether the counters are histograms. I… I think they could be histograms then, because the problem with the histograms was we were… Had a histogram across both of these, but… If they're independent.
metrics, I think you can. I think they can be histograms again.
Golgi Apparatus (us-cam-5cc) 00:10:41 Okay.
Cool, thank you.
Trask Stalnaker 00:10:43 But I also… it's a… I have to think through that.
Since we're kinda… let's tie it back to here, Since we're talking about potentially one met… essentially one metric per… attribute here.
So, would we split? Now, I thought I did, alex… I thought I did limit it to ones that are currently known to exist.
Alex Hall 00:11:21 What I mean is, is it necessary to do that?
Trask Stalnaker 00:11:25 Oh, I see what you're asking.
Yeah, I was just trying to keep it from exploding, but yeah, I agree that the… Idea would be to… Like, naturally, we would extend it.
as needed.
We don't really have this concept of a… template.
It would just kind of be informal.
In terms of how we… A convention for how we name them.
Alex Hall 00:12:08 Right, you know, I don't expect it to be, sort of.
automated in the same way that typical attributes are with the YAML and so on, but… Yeah, something more informal. The way that we have, like, a JSON schema for Input and output messages, and like, yes, there's some machinery around it, but it still ultimately is just some prose saying you must follow this schema.
Liudmila Molkova 00:12:35 We can evolve tooling to do this. We can also immediately have a policy that validates that the naming and, modality in, are aligned.
Jamie Danielson 00:12:49 I guess that's sort of what we have with, like, HTTP request headers, I think.
Where it's, like, a templated thing.
Alex Hall 00:12:58 Yeah.
Trask Stalnaker 00:13:00 Yeah, so the templates… yeah, I did look at that, I remember when, for some options. That only works with the, the arg at the end.
And sort of for good reasons, because then you don't have to deal with pars, escaping and stuff like that.
But I like what Lyudmila's saying, is, I mean, we could have a custom policy in this repo. A custom rego policy is what you're… Thinking.
Liudmila Molkova 00:13:34 Yeah.
Trask Stalnaker 00:13:39 Alex, would you, Would you prefer… it sounds like you would prefer to see the full, kind of, matrix list out of all of them?
Initially, at this point.
Alex Hall 00:13:59 I don't really expect to see a matrix so much as a convention with a few examples.
Trask Stalnaker 00:14:07 Oh, okay, so these are the examples, but there's nowhere that I write down the convention for it.
That's… Sort of what you're getting at.
Alex Hall 00:14:21 Yeah, it's also sort of implied, in a way, you know, don't… We report video output tokens, because we haven't included that here.
Or reasoning image tokens… Or cache write image tokens.
Trask Stalnaker 00:14:52 So, like, combinations that don't make sense, is what you're saying? Sorry, I'm not quite…
Alex Hall 00:15:00 As in, they don't exist now, so they're not in the spec. If they exist in the future.
Just, it might create sort of hesitation.
Liudmila Molkova 00:15:14 It's like, you would like… if somebody wants to report this attribute today, if it makes sense for their model that we are not aware of yet, then they should be free to report it.
Alex Hall 00:15:26 Right.
Jamie Danielson 00:15:27 I think, isn't that generally how we add things to semantic conventions? Is that, kind of, we become aware of a new… thing, and it's proposed to get added in, and there might be a prototype or it already in use, I think that's how we would add it, or is the concern that this list would grow… Exponentially, because of all the new possible.
Alex Hall 00:15:49 I think if we already know what it would look like.
Yeah.
So, whoop.
Trask Stalnaker 00:16:00 We have been trying to limit additions to things that we can… Implement today, or implement reference scenarios for?
Alex Hall 00:16:15 Or is it sort of like a test coverage thing?
Trask Stalnaker 00:16:19 It's… Like, a reality check thing.
There's certainly areas like this where it's like, okay, it's not reality today, but we know that, you know, Sunday it will be, and this is a… we know exactly the shape that we would want it to be in the future.
So, I mean, maybe I can find some, like, a sort of non-normative or someplace in the repo to document the convention…
Alex Hall 00:16:56 I think it's not really, like, a fundamental modeling question of how exactly this is presented, so I think that… I'm fine with just leaving this be.
As for the question of putting these in a complex object instead, If the metrics… corresponded exactly to the span attributes, then I think the answer to that would be no.
Trask Stalnaker 00:17:23 Yeah.
Alex Hall 00:17:24 My vague sense of the advantages of a complex object feel outweighed by… That metrics idea at the moment.
Trask Stalnaker 00:17:35 So I was attracted to complex attribute, when trying to… Split by, like, modality and then cache as, like, kind of these, hierarchical complex attributes, not just a big list of flat things.
But it sounds like we're kind of… I mean, but that ran into all kinds of problems, because it's the… they don't all report those, cross… product.
pieces.
And then, yeah, like, if… it feels like we're kind of leaning into the flat structure here.
Liudmila Molkova 00:18:24 We… we're… We have a rule of thumb to flatten things when we can.
And here we can.
we could represent whatever we have flattened in the same way, but with structure, right? Because there is a structure of some sort.
Trask Stalnaker 00:18:44 Yeah, I was trying to get the best of both worlds and have the structure, the complex attribute naturally fall into flattened hierarchies also.
But…
Alex Hall 00:18:57 So…
Trask Stalnaker 00:18:57 All of my attempts failed.
Alex Hall 00:19:00 Imagine we had… an additional, like, dimension in the future. So right now we have… The dimensions of, like, type, input, output, we have cache, we have modality, those are dimensions.
And there's also the phase thing, but that's only output tokens, there's not… That can't, like, coexist with cash right now, so… Let's say, you know, we added a dimension to deal with tool use.
Prompt tokens, which are, like, an input phase.
And hypothetically, that they could also have a modality or a cache.
And then the attribute might go to, you know, text, cache read, tool use, Input tokens or something.
If… If that appeared one day, then there would be a question of, you know, where do we stick that in the attribute name? What order do we put these different dimensions in?
If there was… Instead, a single usage Attribute that was a list of objects.
Where each object listed all the dimensions.
Then that ordering question could go away.
Liudmila Molkova 00:20:27 To, like, a number.
And what it represents as a… List of properties… Like, 45. To use, paxed.
cash.
Or…
Alex Hall 00:20:49 I think what Trask is writing right now, basically.
So it's like, these dimensions then become an unordered map.
Is this much of an advantage? I don't know.
It lets people, sort of, Add dimensions without… Waiting for a convention, and they still pay a bit of a cost of Like, having to make up their own enum, but otherwise, it's still fairly interpretable.
A flat attribute is also still workable. You know, you just pick an order, and… You can imagine some, like, automated thing interpreting it either way, but… This feels more structured and principled.
Wolfgang Therrien 00:21:44 But I think about, sort of, like, like, the… trying to get, like, the total usage, total token count or something, because maybe that's, you know, a useful signal or whatever, like… This feels like… iterating over the list of tokens that are used there, or filtering over this list, I think, like, seems to map more cleanly to more use cases. It's an interesting… Projection of the data.
Trask Stalnaker 00:22:12 But I wouldn't, I explicitly wouldn't use this for totaling.
Because the… if I recall, the sum of the things overlap in there.
Wolfgang Therrien 00:22:25 Yeah, in a…
Trask Stalnaker 00:22:25 get double counting.
Wolfgang Therrien 00:22:27 Yeah, in a… yeah, I mean, in a perfect world where we had this discrete, you know, well-defined buckets, it would certainly do that. But, yeah.
It's… it's an interesting demo.
Alex Hall 00:22:40 There may be an argument against this, it creates a bit of a footgun.
Trask Stalnaker 00:22:45 I mean, but we would still… we could still report totals…
Wolfgang Therrien 00:22:49 Yep.
Trask Stalnaker 00:22:50 Which… come back.
Alex Hall 00:22:55 You've already put… Like, overlapping in your example.
Like, the last one.
Trask Stalnaker 00:23:09 Yeah.
Alex Hall 00:23:10 Set of the second last.
Trask Stalnaker 00:23:13 And so this… I guess, for a realistic… I forget what the… What was the common overlap problem?
Today…
Jamie Danielson 00:23:32 The cash tokens being included and input for some.
So, input token equals… Regular input tokens plus cash.
Input tokens.
Trask Stalnaker 00:24:03 So, we could have… I mean, we could have this as, like, sort of a detailed breakdown?
But still have, some… Toll… various… whatever totals we think are… Useful…
Golgi Apparatus (us-cam-5cc) 00:24:28 Would you be putting the actual numeric value in each of those objects?
Yep.
Yeah, I think one concern I have with this one, and I don't know about everybody's backends, but… I don't think it would be pretty tough to, query this.
Trask Stalnaker 00:24:55 Like, the idea would be for things that people want to query on.
would be… we would try to stick into totals, although I guess…
Jamie Danielson 00:25:06 But you would need totals for each of them, because they cost different amounts, right?
Alex Hall 00:25:12 I think having a mixture of formats Starts to feel very weird. Look, the complex object thing was… not something I felt strongly about, this was just, like, the one… sort of vague advantage I could think of for it, like, there's a way that it does Provide a bit of a nicer shape, if you, like, assume… Lots of potential complexity.
The flat approach is definitely very workable and simple.
Trask Stalnaker 00:25:43 Okay, yeah, let's… let's try to see if the flattened works out for us for the V1, at least, and… See how complex The industry makes things for us in the future.
Liudmila Molkova 00:26:01 the question of do we also provide aggregates as attributes remains, right? Because how would I sum up all the… input. What… what I use as… Input tokens. How do I know that everything input? I would need to regex attribute names.
And in queries, do a sum of everything that contains input, or have some rule explaining how to sum them up.
Which is… difficult.
Alex Hall 00:26:32 I think it's already in the PR that we would have aggregates, like, you have.
Trask Stalnaker 00:26:36 Yeah.
Liudmila Molkova 00:26:38 I see, yeah.
Cool, yeah.
Trask Stalnaker 00:26:42 And then… Even, I think there was, like, these… Cash, read, input tokens… let's see…
Alex Hall 00:26:53 But also the fact that you have text input tokens, and then text cache.
Trask Stalnaker 00:27:00 Yeah… And it's just because different… to support different providers?
But it does create, you know, kind of… trouble.
Golgi Apparatus (us-cam-5cc) 00:27:36 Just a quick question, maybe, like, Alex, I know there's this Pydantic cost evaluator library.
So I think you probably have a ton of context here. There's no… Real good way to normalize this data.
Like, even with the overlap, is it just impossible to do across providers?
Alex Hall 00:28:01 I don't know what your question is exactly, like, which task?
Do you mean by normalizing?
Golgi Apparatus (us-cam-5cc) 00:28:08 Like, breaking these down so that each measurement is orthogonal, so that we don't have the overlapping counts.
By doing subtraction or some other math.
Alex Hall 00:28:19 I think that the overlapping counts are inherently useful.
Jamie Danielson 00:28:27 I guess maybe it's the lack of consistency across providers where some… Include them and some don't. So the question is maybe not necessarily whether they're aggregate…
Alex Hall 00:28:37 I don't know of any case where providers don't report enough information about tokens for you to calculate the cost.
Like, yeah, I can see the… OpenAI, in some places, it… either reports only audio or only cache tokens, but not the combination, but I think in those cases, that model doesn't actually have a separate price.
both cash for both audio, like, I'd actually be surprised if you can get it.
An output that says, here's the cached tokens, here's the audio tokens.
But not the combination.
In a single request.
Prescott, you're gonna copy all of them.
Trask Stalnaker 00:30:18 Possibly.
Okay, you said, I… cash…
Alex Hall 00:30:25 Dot, dot dot.
Trask Stalnaker 00:30:27 Okay, text output tokens… Okay, okay.
Where were the… where was the reasoning?
So, if we have… All of these… attributes… And we have metric… for… Each one… We're basically… That would be great.
Liudmila Molkova 00:31:21 It will be crazy.
Trask Stalnaker 00:31:29 I mean, can you answer, like, Questions you want, though.
I mean, I guess…
Alex Hall 00:31:44 It seems like that can be very easy to answer any question.
Trask Stalnaker 00:31:51 Sorry, say that again?
Alex Hall 00:31:53 It seems to me that it would be very easy to answer any question.
Trask Stalnaker 00:32:04 What about… what if you're, Using multiple models, and some models… Don't report.
Cache read, cache write… Or you're saying that, essentially, what you think is that all the models That need that. All the cost calculations that need that do provide that.
Certainly should provide that.
Alex Hall 00:32:44 As far as I know, they all do at the moment.
Trask Stalnaker 00:32:52 And comparing this to, so the advantage over… By… Cash here… is essentially… the… confusion aspect.
That here…
Alex Hall 00:33:24 we are.
Trask Stalnaker 00:33:24 Putting back.
Alex Hall 00:33:25 It took me a while to understand how it works, and I understand that… I mean, sort of.
kind of get it. But even then, as far as I could tell, it doesn't actually… But if… If there are cases where you don't have Like, that data info, the joint data.
It seemed like these multiple counters were meant to solve that case, but they didn't actually fully solve it.
Trask Stalnaker 00:34:03 Well, so they were meant… the way that I intended was that it would… You could still roll up things.
By… modality… Or buy cash.
If you wanted to, within… that metric.
But… maybe what you're saying as far as… I mean, as far as getting cost metrics out of it, which is… Sort of the important thing, or at least a… Proxy to CAG… to cost.
Maybe the question is, why would you want to roll up over One of those dimensions, because now you're… Essentially, you're losing your cost.
proxy.
Liudmila Molkova 00:35:11 I have a naive proposal. Tell me that I'm wrong.
So, people… Wouldn't… the only reason people care about each particular breakdown is because they want to reaggregate it using some additional information into cost.
And what they want is a cost and breakdown, maybe, for this cost to understand where the cost comes from.
What if we don't need to provide the metrics?
But I provide them… Logs with details, and let them aggregate these logs into whatever costing they want.
Alex Hall 00:35:54 What?
Trask Stalnaker 00:35:56 Sam… wouldn't sampling… Kill you?
Liudmila Molkova 00:35:59 Logs.
Trask Stalnaker 00:36:04 assuming you're… I mean, my default stance is to sample logs along with traces.
Although I know that's… that's, like, a 50-50.
proposition.
Golgi Apparatus (us-cam-5cc) 00:36:26 What's, like, the motivation for the question?
Liudmila Molkova 00:36:32 I think it's if we have 20 metrics.
with… and this list is essentially dynamic. It depends on what you… what you are.
provider supports.
Writing a query around it is tremendously difficult.
It's not the… common user problem. They would need something like Pyidentic Cost Library to make sense out of this data.
Trask Stalnaker 00:37:03 I mean, we could do, we could do a single metric.
And these could… the span attributes, we could essentially just use as metric attributes.
And… say that… No, it's, cardinality.
What's… Can we do… counts… I mean, we would lose aggregation across… Aggregation would be meaningless.
But could we even do it if we accepted that?
Alex Hall 00:37:44 And are you essentially making… an attribute.
That is equal to what would have been metric name.
Right.
Liudmila Molkova 00:37:59 Yeah.
Trask Stalnaker 00:37:59 would be the… the… yeah.
So taking all of those span attributes have, mega Counter.
input tokens.
Wow, but these are… these are attributes, they can't… that's not values.
Alex Hall 00:38:30 Where it sounds like you'd have an attribute like type equals.
Text cache input.
Liudmila Molkova 00:38:36 Alright.
Alex Hall 00:38:46 I worry about breaking the summing rule, because people might be very tempted to just… Some of the values without looking at the attributes.
Jamie Danielson 00:39:08 Do you mean, like, summing without looking at the fact that there are different types of, Tokens or whatever, so there are gonna be different costs.
Is that what you're…
Alex Hall 00:39:19 No.
Trask Stalnaker 00:39:20 overlap.
Alex Hall 00:39:20 They take the sum, they don't get a meaningful total. Whereas right now, they do.
Jamie Danielson 00:39:25 Yeah.
Liudmila Molkova 00:39:29 No, they… Don't, because… Because they need to filter, like, filter by the… the… Type, but yeah.
Alex Hall 00:39:41 No, I mean, if you add up input and output tokens, you get a meaningful number.
Liudmila Molkova 00:39:53 Yes, if you first filter by input, and then filter by… okay, anyway, so yeah.
It seems…
Alex Hall 00:40:03 I don't know how meaningful it is as a metric. It's meaningful when you do it on a span, you add up input and output tokens, it gives you something that sort of gives you a sense of how full the context window was.
As a metric, I don't really know what you'd be measuring if you did that.
Liudmila Molkova 00:40:21 And as an easy-to-digest thing, we should still provide the input and output tokens, probably, as metrics of some sort.
Like, aggregate. So I… you don't want to look into the details, like, your first… Shot this there.
Yeah, Erin.
Golgi Apparatus (us-cam-5cc) 00:40:44 In the interest of, like, strawman proposals for you all to tell me it's a dumb idea. We also have, like, the unit. Unit is identifying.
if you converted this… I don't think it's a good user experience, definitely not with certain backends, but if you do, like, the Prometheus metric mapping, the unit ends up in the metric name, right?
So, like.
Liudmila Molkova 00:41:11 Yeah, she read… yeah.
Golgi Apparatus (us-cam-5cc) 00:41:13 Yeah, the reason that some of these can't be added together is because, like, maybe semantically they have different units, and then… Likewise. I mean, I don't think it's a great suggestion. What do y'all think?
Trask Stalnaker 00:41:30 And… understand the suggestion. Sorry.
Alex Hall 00:41:35 Yeah.
Golgi Apparatus (us-cam-5cc) 00:41:36 The suggestion was to put unique units for, for these metrics that can't be added together.
So that they could keep the same metric name, but if you record it with different units, you would get, distinct metrics in the backend.
Alex Hall 00:41:53 I mean, not… Oh, God.
Trask Stalnaker 00:41:55 No.
I don't pick up.
Golgi Apparatus (us-cam-5cc) 00:42:01 For me, this, it looks okay, to be honest, but yeah.
Trask Stalnaker 00:42:05 But a lot of other backends don't do that.
Liudmila Molkova 00:42:20 So it sounds like, if you want a detailed experience.
Sorry, detailed information. Your experience is going to suck.
in a different ways. Either it's a mega counter, and you… Need to know how to filter it, or you need to know upfront.
All this interesting metric names and understand how to aggregate them properly.
Alex Hall 00:42:48 Well, if there's many metric names, yeah, you don't… have to aggregate them. You don't… you don't combine different metric names, you don't have to do anything within the metric names unless… except in terms of, you know, models or whatever, but you don't… you no longer have to think about aggregation, about modality.
Liudmila Molkova 00:43:09 So then, if you… Don't care about the breakdown, you just use the metric that's already reported as aggregated over this modality.
Alex Hall 00:43:18 Yes.
So are you saying that there's some, like, backends or something where, you know, having a large number of Metric names like this just wouldn't work well.
Like, they expect it to be very… Well-defined, very, very low cardinality.
Trask Stalnaker 00:43:43 It's not so much a back-end limitation, because, I mean, it's still… more or less… The number of time series that you're… in total capturing. It's not, like, a large number of metrics for backends to handle. I think more it's just conceptually… For users… having to… Navigate over all of those different… Metrics. Know a… know that there are so many different metrics Involving so many different metrics into their queries.
Is the concern.
Liudmila Molkova 00:44:28 And then, if… if they don't… if it's… if you group them, then people need to know how they are grouped.
And would need to know the variety. Well, knowing all possible values of an attribute is easier. Like, all the possible values that you have in your backend is much easier than Knowing all metric names.
Trask Stalnaker 00:44:48 Right, which is what I like about the Mega Counter.
At least you could query and get all the different types of things that are getting reported.
Alex Hall 00:44:59 Is knowing automatic names hard? I expect that to be an easy operation.
even a UI-supported operation.
Liudmila Molkova 00:45:09 Data complete.
You mean?
Alex Hall 00:45:12 Right.
Okay, I…
Trask Stalnaker 00:45:17 I think most metrics, like, you would need to know that you would put the metric name into your query.
Like, metric names aren't… are oftentimes not dynamic.
Liudmila Molkova 00:45:32 Like, it's easy to write, Duration by that attribute, and you would see the breakdown by that attribute and all possible values.
But for metrics, you need to know the prefix, and you need to guess the prefix right.
Where you need to issue multiple queries.
Essentially.
The mega counter, is it a counter or a histogram? Do we still need histograms?
Trask Stalnaker 00:46:19 I think it's a counter.
For you to… if you want to be able to do, Cost calculations from it.
Liudmila Molkova 00:46:31 And then, what if… the mega counter is ONLY about the breakdown.
So, the things like input tokens don't appear in MegaConter, they appear as a separate metric.
So, you can choose to have an easy-to-understand metric without details.
Mega Counter can even be opt-in, and then you would see all possible breakdown in it.
Golgi Apparatus (us-cam-5cc) 00:47:05 I'm still a little lost on the mega counter, because if we're throwing out the… the aggregation across all dimensions rule, then I feel like we're back… we might as well just do the thing that we had at first.
Trask Stalnaker 00:47:20 I think this… we've veered into solving, like.
What we have at first doesn't solve some of these questions.
Liudmila Molkova 00:47:31 Yeah.
Trask Stalnaker 00:47:31 It does… it didn't have break… there's no breakdown by modal… by modality, or cache or phase in the current.
Right, right.
Golgi Apparatus (us-cam-5cc) 00:47:42 Sorry, I meant the proposal to just add them as attributes.
Alex Hall 00:47:53 I think that the mega counter lets you have… the multiple levels of granularity. You can have just cache, just modality, or cash and modality.
Trask Stalnaker 00:48:08 Aaron, I didn't, follow what you were asking about adding all the attributes.
Golgi Apparatus (us-cam-5cc) 00:48:16 If you just… if you just group by… Nothing, then the sum across all of them would have the double counting still, right?
Trask Stalnaker 00:48:24 In the mega counter, yeah, there would be some problems.
Golgi Apparatus (us-cam-5cc) 00:48:29 Yeah, I didn't fully get what Alex said there, but I'll think about it. The only other thing I wanted to say was the histograms do have a counter embedded in them, so if… I think it's pretty much always okay to use that one if you have a distribution of values that are summable.
Trask Stalnaker 00:48:59 I see. Yeah, I think I understand what you're saying.
Golgi Apparatus (us-cam-5cc) 00:49:02 Yep.
And I think in… I think it's a sum field, you don't have to, like, do anything fancy. And for Prometheus, I think it gets turned into a separate count metric that looks just like a counter.
Liudmila Molkova 00:49:16 some… Or a title.
Trask Stalnaker 00:49:23 Yeah, and you can still get the sum… Per time series.
Yeah, okay, I make… I understand, yes, yes. I think it… I think it could be a histogram also if we're, I mean, essentially throwing away that.
aggregation rule.
Which… these… Metrics were designed to Not… to not throw that away.
But that's also why… Potentially, they're more… complicated.
Golgi Apparatus (us-cam-5cc) 00:50:23 I guess maybe one other thing to throw out is, what if optionally we provided, I know it's not ideal, but if we provided, like, a cost metric that did the calculation on the client side as an optional thing.
To… because consuming these metrics is going to be a bit difficult right now.
Trask Stalnaker 00:50:45 That would be nice, but I don't know, I don't know how we would get cost.
Alex Hall 00:50:49 That's a weirdo.
Trask Stalnaker 00:50:53 Sorry, what, Alex?
Alex Hall 00:50:55 That's what we're doing, we're calculating costs in the client, and we create both the span attribute and a metric.
Trask Stalnaker 00:51:02 Oh, in the client, you actually calculate cost?
Alex Hall 00:51:05 Yeah.
Golgi Apparatus (us-cam-5cc) 00:51:06 Yep.
Trask Stalnaker 00:51:09 Do you release new clients, then, as costs change and models get added?
Alex Hall 00:51:15 There's a separate library which has essentially a database of costs, and maintaining it is an absolute pain.
And it has plenty of gaps.
Liudmila Molkova 00:51:28 Could make a cool collector predecessor.
Alex Hall 00:51:32 It is a very difficult modeling problem.
There could also be one histogram per… like, exact type of breakdown. You could have.
you know, the simple one like right now, you could have one by cache, and it only has a cache attribute, no modality attribute. There's one by modality, it doesn't have a cache attribute, and there's one by cache and modality.
And so each of them can be assumed.
Within that particular metric name.
But they have different levels of granularity, so they overlap with each other.
Trask Stalnaker 00:52:43 And what would we… Due for, providers that report the cross product, the join.
Alex Hall 00:52:53 There would be another histogram, cache and modality.
Liudmila Molkova 00:53:01 And then, if we add two years, This would grow combined… Torically.
Right?
We'll be interesting.
Alex Hall 00:53:11 Almost the same way as everything else would.
But not quite as explosive as, for example, one metric name per Every combination of values.
Liudmila Molkova 00:53:23 Right.
Trask Stalnaker 00:53:27 Ludmila, what was… if we add what?
Liudmila Molkova 00:53:31 the tool use.
Trask Stalnaker 00:53:32 Totally, it's.
Liudmila Molkova 00:53:33 Oh, yeah.
Alex Hall 00:53:37 I think the tool uses more like adding phase to input tokens.
But I guess that's still… Potentially another.
Golgi Apparatus (us-cam-5cc) 00:53:51 What did you mean by phase?
Trask Stalnaker 00:53:54 The way I modeled, reasoning tokens in this PR is I called it a phase.
For the output tokens, whether it's a reasoning token or not.
Golgi Apparatus (us-cam-5cc) 00:54:06 Gotcha.
Liudmila Molkova 00:54:11 Also, essentially, a fair… Think about the metrics.
I think the operation type is also part of it, so the inference is part of it, the embeddings would be part of it.
At that list.
That they are, it's easier.
Okay, so this… this metrics will be different, and… then… We would consider having the agent token usage, maybe one day.
But… Then, some of these concepts would not apply, like cash.
Probably. It's the model.
Alex Hall 00:54:51 I don't know what… You'd have agent tokens for.
Trask Stalnaker 00:54:58 So the…
Liudmila Molkova 00:54:59 Oh my god.
Trask Stalnaker 00:55:00 Oh, go ahead.
Liudmila Molkova 00:55:02 No, go ahead.
Trask Stalnaker 00:55:04 right now, we are reporting tokens on Invoke Agent.
spans… Which causes some confusion for some people, I think they can add up token usage across a span.
Alex Hall 00:55:23 Right, we specifically had to… Deal with bets.
Hmm.
Trask Stalnaker 00:55:28 Yeah…
Alex Hall 00:55:29 And I wasn't even sure if, like… Goodbye.
Decision was sort of settled, or, like, confirmed that we want to keep it that way, or… Yeah.
Trask Stalnaker 00:55:38 I want, we were… Ludmil and I were just chatting about this yesterday. I… I would like to find a… way to… Sidestep that problem, because we've seen too many people fall into that, hit that as a problem.
So yeah, if you have suggestions, would love to hear them.
Alex Hall 00:56:03 We have an option to use, like, a slightly different attribute name.
On the agent span attributes.
So that it's clear that it's different.
Liudmila Molkova 00:56:18 I think the… the idea… Now was that we would remove the… attribute from internal agent spans?
And with, like, hostage agents, presumably, at least today, you don't… it's like the inference call, you're calling something external.
But it's still… people are still interested in Knowing… In having an aggregate number.
On the agent of how many tokens it burned in the nested calls. Maybe if we propagate agent name to the inference matrix, it would be… important.
Trask Stalnaker 00:57:11 Would that, Alex, would that resolve the… is the issue you've had only on the Invoke Agent internal spans?
Or do you also see an issue? Because we were thinking with client spans, invoke agent client spans, it's more natural to capture them there.
Alex Hall 00:57:35 Yeah, I think it's fine if you don't also have, like, children's bands Which are double commenting.
Trask Stalnaker 00:57:47 What if that child span… what if you're… also, your distributed trace has the… server… the invoke agent span, kind of, on the server side, and…
Alex Hall 00:57:59 No, I think that comes back to the same problem.
I mean, we don't have this concept of, like, remote agents in our framework like this.
So…
Liudmila Molkova 00:58:12 If someone, got forbidden instruments.
the model hosting clear, which VLM does, I think, then you would have the same problem with inference. You cannot Some tokens across the whole… Trace 3.
I was sort of…
Trask Stalnaker 00:58:43 thinking of it like HTTP… server duration, HCP client server duration.
That those sum up well within one host, but as soon as you, you know.
propagate downstream, now you have, sort of, duplicate overlapping HTTP span durations.
But that may not be how… I mean, it can… how people are thinking about tokens. I think the overlapping durations is… Been around for so long that people are used to that mental model.
Golgi Apparatus (us-cam-5cc) 00:59:27 I think it's kind of… Unless you do it with, like, a really fancy query, it's kind of… hard-to-solve instrumentation, because you don't know what the downstream of you is gonna do. It's gonna… Count or not, so… I almost feel like the easiest thing is, if you were writing a query over the graph, you could… we could describe some rules to do it correctly, or something like that.
the, the spend graph.
Trask Stalnaker 00:59:55 Yeah, I guess the question is, is there anything we can do on a modeling side to make that easier?
But…
Liudmila Molkova 01:00:05 Aggregate.
Aggregate tokens, it seems what it tells people to do is to not sum them up.
But if you have, like, nested agents.
Then you would still be interested in querying them.
And would you sum them up?
Well, the rule is you don't sum up aggregated, the outer contains everything.
Trask Stalnaker 01:00:35 I want to be respectful of everybody's time here. I, really appreciate everybody joining in here, and… I got a lot of good things here to… give me a day or two to, I will, try to digest all of this, and regurgitate something back onto the PR.
And we can, go from there.
Liudmila Molkova 01:01:10 I'm looking forward to hearing back from you on Sunday.
Two days.
Golgi Apparatus (us-cam-5cc) 01:01:16 Alright, thanks, everyone.
Trask Stalnaker 01:01:17 Who knows?
Jamie Danielson 01:01:20 Thanks for this.
