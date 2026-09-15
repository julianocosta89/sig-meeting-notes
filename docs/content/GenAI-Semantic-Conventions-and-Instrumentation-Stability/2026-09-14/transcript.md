SIG: GenAI Semantic Conventions and Instrumentation Stability
Date: 2026-09-14
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 01:22 Hello.
**Trask Stalnaker (Microsoft Corporation)** 01:25 Hey, hey!
**Surya Teja** 01:31 Hey, hi folks!
**Ankit Singhal** 01:37 Mmm…
**Siri Varma** 01:47 Hello.
**Trask Stalnaker (Microsoft Corporation)** 01:51 Hey, everyone.
**Neil Yashinsky he / him** 02:05 Just hang on now? Oh.
Hello, Vern.
Is this coming through now?
**Trask Stalnaker (Microsoft Corporation)** 02:10 Yeah… Neil Yashinsky he / him 02:11 Hey, Trask Clover, I'm sorry about that.
**Trask Stalnaker (Microsoft Corporation)** 02:12 Okay, no worries… What is happening with my sharing? Please move this away from shared… Hang on.
I will get this right.
**Liudmila Molkova** 02:31 I can share a few… If you're having problems.
**Trask Stalnaker (Microsoft Corporation)** 02:38 I… I can… I can technology.
**Liudmila Molkova** 02:47 Screen sharing and Bluetooth are not… Not technology.
**Trask Stalnaker (Microsoft Corporation)** 02:51 And wireless printing.
**Neil Yashinsky he / him** 02:53 Oh, man.
**Liudmila Molkova** 02:54 tank.
**Neil Yashinsky he / him** 02:54 I feel like that's the great boundary, no matter how technically proficient you are. If someone asks you to say, oh, I'm kind of having problems with my wireless printer, can you help me? I feel like most people are even gonna be, like, the smartest developer, engineer, whatever, DevOps, you're like, oh… Is that a driver issue? Oh…
**Trask Stalnaker (Microsoft Corporation)** 03:17 Cool, so why don't we jump in? I started to write some… notes on… This usage one, so, Rivet can… Help to… Drive on the display.
discussion here… Okay, so… We've got… The core problem here is… We've got our input tokens, output tokens per operation.
That we want to capture as histograms.
And we've also got a bunch of counters that we want to capture.
These… 2… In theory, are the same as these two…
**Liudmila Molkova** 04:17 accept the… Bottom one are permodality.
**Trask Stalnaker (Microsoft Corporation)** 04:23 have dimensions.
**Neil Yashinsky he / him** 04:25 Did you say per modality, Ludmila?
**Liudmila Molkova** 04:28 Yes.
**Neil Yashinsky he / him** 04:29 Interesting. Okay, thank you.
Oh, so, like, packs versus…
**Trask Stalnaker (Microsoft Corporation)** 04:35 audio.
**Neil Yashinsky he / him** 04:36 Perfect, thank you.
**Trask Stalnaker (Microsoft Corporation)** 04:37 Yeah.
It's a weird word, modality.
And so… The, we've got… This usage dot in here And we've got this detailed dot in here.
And… the usage… is… kind of nice… As a namespacing, like, concept.
Especially when there's lots, potentially lots of them under there.
Because… Right.
Certainly, there's an option of putting input tokens, not having dot usage there.
But it is a nice… I understand that grouping.
perspective.
**Liudmila Molkova** 05:36 it is, I think, more than nice, because If we drop it… then the attributes that also have usage would look like GenAI.
Input tockets.
Which… is… It feels like it's not… That's not, it's not specific to something.
**Trask Stalnaker (Microsoft Corporation)** 06:01 We wouldn't have to drop it on the attributes, though.
**Liudmila Molkova** 06:06 Okay.
Okay, yeah. So, yeah, that's an option.
**Trask Stalnaker (Microsoft Corporation)** 06:11 The namespace doesn't match the attribute namespace anyways.
**Liudmila Molkova** 06:17 Agree, yes.
**Trask Stalnaker (Microsoft Corporation)** 06:21 And then the other question here, we've got detailed dot… well, we need some way to differentiate these two from this set.
Right.
So, the current proposal is detail.
So, I think I, I, I definitely understand.
Where… where you came up.
With this, and why.
I was trying to play around with, like, it's so long.
If we needed, like, what it would look like Without usage here.
And, like, it kind of looks okay with, like, duration. We've got inference.duration and inference.inputTokens and output tokens.
But, like, if we in the future had a lot of these… if we had the multiplicity of these token breakdowns, Then, you know, that namespace starts to be… Pretty nice.
the other…
**Liudmila Molkova** 07:33 Push.
**Trask Stalnaker (Microsoft Corporation)** 07:33 Okay.
Oh, yeah, go ahead.
**Liudmila Molkova** 07:38 It would still be clear, like, if we drop usage, it would still be clear, because there will always be suffix input tokens or output tokens.
**Trask Stalnaker (Microsoft Corporation)** 07:53 If we did that, if we dropped usage here, Would you… Would… would it be weird to keep usage here instead of detail?
or detailed, Like, can you… What does the word detailed mean? And first, Aaron, please jump in.
**Liudmila Molkova** 08:17 Oh, you're muted.
**Aaron Abbott (Google LLC)** 08:19 No, no, please respond to that. I'll go after it.
**Liudmila Molkova** 08:23 So, I'm… The detailed here means the breakdown, because those are broken down by whatever Where… Wanted to be broken down.
The… other point, so we… I don't think it's meaningful it's necessary to… necessary to express the… that it's a breakdown. I think the main need is to differentiate.
And… we can… Differentiate in other ways.
And we can even put the count here.
Either before input tokens or after input token.
worry.
Yeah.
**Trask Stalnaker (Microsoft Corporation)** 09:21 Oh, yeah, related to that, another option, Instead of doing the count, Here would be… Leaving these as is, and this could be input tokens per operation.
**Liudmila Molkova** 09:43 Okay, dot or underscore?
**Trask Stalnaker (Microsoft Corporation)** 09:49 But that's summing them. I was gonna say underscore, but then the sum is weird.
Yeah, I don't know.
**Liudmila Molkova** 09:59 Oh, pull that right?
**Trask Stalnaker (Microsoft Corporation)** 10:01 The input for operation…
**Liudmila Molkova** 10:09 The sum is fine. It's the same, it's just the name change, right?
**Trask Stalnaker (Microsoft Corporation)** 10:14 Yeah, I was just thinking of, like, the… the sum, the name of the sum.
In… per operation, I guess… Probably fine.
**Aaron Abbott (Google LLC)** 10:32 But.
**Trask Stalnaker (Microsoft Corporation)** 10:32 Operation… oh yeah, go ahead.
**Aaron Abbott (Google LLC)** 10:34 Oh, sorry, I was gonna say Ankit. Yeah, yeah, I mean, I asked that question in chat, but then I think Ankit.
wanted to say something.
**Ankit Singhal** 10:45 Yeah, so actually, I just shared, like, another link, I think I shared that before, about, like, the dimension of, short context and long context, because, pricing for input, same time for tokens differ in that case, so… And I don't know if that also would be a consideration, just to design here, so that in case dimensions like this come in the future, we can handle without having it.
**Liudmila Molkova** 11:08 Ankit… I did the research based on your previous thing. It's linked somewhere to the PR. The long story short.
it is not a good dimension for the OpenAI, because it's essentially one-on-one per model. So, for Astra, you always have Oh, sorry, you piqued it in some other way. Interesting. For Anthropic, they do have it as a choice. You can choose for any model, you can choose short or long context.
And it can be a dimension, another dimension on the counters, not on the histogram.
So, it fits nicely, we just need to define an attribute for this eventually. I created an issue to track all the… other billing-related things that are available across, like, major providers. I'll dig it up in a sec. But I think the design for this matrix allows it, but I don't want to introduce new concepts.
Yet, let's just figure out what… what, like, finalize the design knowing it works for things like this.
**Ankit Singhal** 12:17 And then, the part that you mentioned about the, counter, so, like, I think… I'm guessing the idea is it makes more sense on the counters to have this, so that… aggregation of the tokens, and then finally a price of it, right? Or…
**Liudmila Molkova** 12:33 It's… we cannot have this on histograms unless we want to name histogram per everything. The number of tokens for operations that have short context and,
**Ankit Singhal** 12:48 Oh, I see.
**Trask Stalnaker (Microsoft Corporation)** 12:49 video.
**Ankit Singhal** 12:49 Okay, got it. Okay, so input tokens, yeah, then they have, like.
two dimensions, short, long, and then if anything comes along, then you're breaking down the histogram.
**Trask Stalnaker (Microsoft Corporation)** 13:04 Yeah, we basically can't have any dimensions on these.
**Ankit Singhal** 13:07 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 13:08 diagrams for those complicated reasons that.
**Ankit Singhal** 13:12 Got it. Okay, so I think then… then it makes sense on the counters, right, whenever they… because of… because that's how you would probably get to the pricing finally, right?
Okay, sounds good. Thank you.
**Liudmila Molkova** 13:26 I'm posting the comment with a link to additional, stuff that we should probably add at some point, in the chat, in the Replying to your comment, Ankit.
**Ankit Singhal** 13:39 Thank you. Appreciate that.
**Aaron Abbott (Google LLC)** 13:48 One thing I wanted to call out was… or… I think for most runtime metrics, we have whatever the thing is, and then dot usage.
I think they're usually counters, so, for example, I think… It's really quick, like… see if I can find one.
Hardware, power supply, dot usage, Container.cpu.usage,
**Liudmila Molkova** 14:11 Yeah, it's a great point. The usage there is different usage than usage here.
Usage there is like a semantic convention, suffix to say that it's the… the ratio, right?
**Aaron Abbott (Google LLC)** 14:27 This is… this would be the numerator of the utilization, right?
**Liudmila Molkova** 14:31 Right.
**Aaron Abbott (Google LLC)** 14:36 I think I might have written this.
**Liudmila Molkova** 14:39 Nice.
And for here, usage is the… what AI providers call usage.
Maybe it's a good idea to drop it, so it's not confusing one with another.
**Trask Stalnaker (Microsoft Corporation)** 15:00 I would… yeah, I thought it might be a problem, but then I convinced myself it wasn't, because we're using it as a namespace.
Instead of a leaf node, but yeah, if there's something… We have another option. Oh, well, we're thinking of dropping… potentially dropping it.
**Aaron Abbott (Google LLC)** 15:20 Yeah.
And just for… Like, as devil's advocate, why is it different than usage of other resources?
**Trask Stalnaker (Microsoft Corporation)** 15:30 Oh, as in me.
**Liudmila Molkova** 15:35 Sorry, Trask, go ahead.
**Trask Stalnaker (Microsoft Corporation)** 15:38 Why it's different than resource?
Usages?
**Aaron Abbott (Google LLC)** 15:45 Like, why is… token usage different from, like, CPU time, for example.
**Trask Stalnaker (Microsoft Corporation)** 15:51 Oh, I had convinced myself it was okay for us to use usage here, because it's a namespace.
Right, as opposed to dot usage.
like, as a, I think that these conventions, the naming here… Generally refers to dot usage being the leaf…
**Aaron Abbott (Google LLC)** 16:20 Right, okay, so we're saying… we're saying because there's no limit to the amount that we shouldn't use this usage pattern, is that right?
**Liudmila Molkova** 16:29 Yeah, so this usage pattern is for, part of a known total, designated with some state.
**Aaron Abbott (Google LLC)** 16:38 Right.
**Trask Stalnaker (Microsoft Corporation)** 16:39 So we shouldn't use token.usage.
I think, according to this, we shouldn't use token dot usage.
But I would say that usage.tokens is, Not really clear whether we can use that or not.
I kind of think that maybe it's okay, because it's a namespace, as opposed to… All these other things here are… Meant to be, like, the last name in a metric.
**Neil Yashinsky he / him** 17:17 Erin, is there a question that… There needs to be, a parent namespace to hold tokens, and this would be one of them.
**Aaron Abbott (Google LLC)** 17:29 No, no, no, I just wanted to, like, disambiguate this from the other usage metrics, and I think the… it sounds like the answer is because there's no limit to the tokens for this, and there's no, like, corresponding utilization metric, we shouldn't follow that other Semantic convention. And then, I think Trask is saying, because it's not used as the suffix.
There… then you should… it's not the same convention, and it should be okay.
**Neil Yashinsky he / him** 17:52 Thank you for reading me in. Okay, I appreciate that.
**Liudmila Molkova** 18:01 Okay, usage or not. We need to find a word instead of detailed, and it can exist with the usage or without usage, and that's the, I think, the trickiest problem.
**Trask Stalnaker (Microsoft Corporation)** 18:13 Okay, so we've got… Neil Yashinsky he / him 18:15 The one question that I… It's like, is this… is it resource?
or something? Is that, like, the detailed view that we're looking into? Not to necessarily say resource should be the namespace, but I feel like that's what we're… reaching for, like, detailed is the detailed usage in this case, but I feel like that's not the whole use case, it's just a… You know, one of them?
**Liudmila Molkova** 18:47 Not sure I understand.
**Neil Yashinsky he / him** 18:49 So, we're looking for a replacement for Detailed.
Is that, like, kind of the essence of this? We don't want to use detailed. Usage could be it. We're trying to finalize on if usage is the replacement for detailed? Is that the crux of this?
In a sense.
Because it can't be histogrammed in the…
**Ankit Singhal** 19:10 Oh, okay.
**Trask Stalnaker (Microsoft Corporation)** 19:10 I think that… let me write down some,
**Ankit Singhal** 19:13 Options.
**Neil Yashinsky he / him** 19:15 Thank you, Trask.
**Trask Stalnaker (Microsoft Corporation)** 19:17 We'll call this option A, which just drops, drop usage…
**Ankit Singhal** 19:25 Oh, shit.
**Trask Stalnaker (Microsoft Corporation)** 19:26 B… We, something.
Ankit, we've got some background noise there.
Detail, replace, a new word, Or detailed.
I mean, these are the two options we've thrown out so far.
**Yeah, so… Neil Yashinsky he / him** 20:00 to maybe just clarify, that's really helpful, Trask, thank you. So, like, yeah, that was my… I think option B, like, we need a replacement for detailed.
Is it usage or not, I think was maybe the question, the first question we asked? It's like, is usage good enough, or people don't like usage, and then we can find something else.
If I'm understanding the conversation, I'm not trying to lead it, of course, just trying to… Are there other… Facets.
of usage… And or detail that could fill out the bottle further that would inform our decision? Did anyone think of?
So it seems like it's… we're, like, focusing on one child, and it kind of, like, if we're defining the parents, we should talk about the other children? Is that… Sensical?
**Trask Stalnaker (Microsoft Corporation)** 21:11 Let's… sorry, I just want to throw in, per… Operation, or per infer… per… inference, while we're throwing out all the op… all the possible options.
**Neil Yashinsky he / him** 21:27 No, that's beautiful, yeah.
**Trask Stalnaker (Microsoft Corporation)** 21:34 What was this, then?
Oh yeah, then we could just do… That, possibly.
**Liudmila Molkova** 21:49 Name this, this is the… pretty much equivalent of GenAI client inference operation.
input tokens.
the previous version of the PR.
So, operation as a namespace, not a.
**Neil Yashinsky he / him** 22:10 Right.
**Liudmila Molkova** 22:10 preparation.
**Neil Yashinsky he / him** 22:13 There's some…
**Trask Stalnaker (Microsoft Corporation)** 22:13 Oh, yes, and so that kind of comes up against the 243.
**Liudmila Molkova** 22:22 It… like, the version you have… none of them, actually. Oh, right, yeah.
I see, yeah.
With 347…
**Trask Stalnaker (Microsoft Corporation)** 22:36 I got the wrong number.
**Liudmila Molkova** 22:45 So it should be somewhere in the options, maybe it was option 1 at some point, it's in the PR description somewhere.
Well, yeah, here.
**Trask Stalnaker (Microsoft Corporation)** 22:53 49th.
So, yes, so we're… We want to split this.
And the question whether we need to keep operations sort of starts feeling redundant.
Or we're naming the operations.
As what we're doing.
**Liudmila Molkova** 23:21 Yeah, but I mean, the GenAI inference… a GenAI client inference, Operation… input tokens.
would stand out, but GenAI client inference, input tokens, preparation would also stand out, which… which is probably… but in… Maybe in a good way.
So, like, you probably… should be using counters. The counters are the… where all the cost analysis would be based on.
And you only need histograms to find out layers.
And it puts them into some advanced category.
That we don't want people to look that much into, and having an awkward name for it, like, underscore preparation.
subjectively puts them in, like, makes them more advanced.
So maybe… In this sense, picking the GenAI client inference input tokens for counters.
We, we can.
Stick to this.
And then just figure out… Preparation or whatever else for histograms.
**Trask Stalnaker (Microsoft Corporation)** 25:02 So, we've got duration… Okay, so this is kind of where that… where that would take us.
**Liudmila Molkova** 25:49 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 26:11 I guess, that's…
**Liudmila Molkova** 26:12 Yeah.
Yeah, if we can keep the operation.
And… We can even potentially keep it for the inference operation duration, where it's kind of… Of this.
**Trask Stalnaker (Microsoft Corporation)** 26:45 And with this 249… Let's see, the… So we're proposing… Embeddings, retrieval…
**Liudmila Molkova** 27:12 There'll be a lot of operations that don't feel important.
**Trask Stalnaker (Microsoft Corporation)** 27:18 Yeah, yeah. I, I like… I liked this idea where… This… we're, like, naming the operation.
And we have the natural… duration… I mean, in… Inference operation… This… I mean, I understand what you're saying about prioritizing that name.
And so, I think that's a… A good reason for making this tokens, but the consistency piece of me wants this to match with duration.
as, like, The histograms, the input tokens per operate, like, if this is the operation.
Then this is the input tokens.
**Liudmila Molkova** 28:27 How do you feel about inputtoken.count?
**Trask Stalnaker (Microsoft Corporation)** 28:34 count.
**Liudmila Molkova** 28:35 So this is the replacement for detailed.
And it's… It's kinda… maybe explains more what's different between the counts and histograms. We don't outline the histograms.
as histograms.
**Aaron Abbott (Google LLC)** 29:06 Isn't there, like, a… Some guidance that specifically says not to do that.
**Liudmila Molkova** 29:12 Not to put count? No, there is a guidance that says to put count for… For counters, but for up-down counters.
**Trask Stalnaker (Microsoft Corporation)** 29:20 confusing.
Yes, yes, I guess for up-down counters, just definitely not.
Okay.
**Liudmila Molkova** 29:28 Not… not plural, that sometimes leads to counter… to those.
**Aaron Abbott (Google LLC)** 29:32 Right.
Yup.
**Trask Stalnaker (Microsoft Corporation)** 29:41 Okay.
**Liudmila Molkova** 29:42 InputToken.distribution and inputtoken.com.
**Ankit Singhal** 29:53 Could be the distribution part?
Sweet.
**Trask Stalnaker (Microsoft Corporation)** 29:58 the histogram.
**Ankit Singhal** 29:59 Oh, I see.
**Liudmila Molkova** 30:02 Or histogram.histagram.
**Trask Stalnaker (Microsoft Corporation)** 30:11 No bad… no bad ideas here.
**Ankit Singhal** 30:17 To be honest, I also like GenAI inference.operation.inputTokens.
I met him.
**Trask Stalnaker (Microsoft Corporation)** 30:27 input tokens.
It's not a bad, like, I mean, that doesn't mean we have to… use Operation Everywhere. It could just be, like, If there's ambiguity, We do operation…
**Liudmila Molkova** 30:50 Yeah, it helps us differentiate. It solves this part of the problem. The part of the problem it doesn't solve is that, it's still, like, if I'm a user, I'm looking into the two of these things. I need to have an idea which of them is which.
And it solves, maybe, some part of this problem.
But I also don't think, like, that the solution between distribution and cloud is an excellent one. Users who Like, are new to this, they would have equally bad experience knowing what the difference between content distribution is.
**Trask Stalnaker (Microsoft Corporation)** 31:29 Do you think usage.inputTokens versus operation.inputTokens?
**Liudmila Molkova** 31:40 I… I actually… my thoughts are that we have a lot of options. None of them are obviously good.
they're almost equally bad, and I'm happy with this approach. I think whatever we will decide will be bad in some sense, and we will live with that.
**Ankit Singhal** 32:00 I wanted to add one more thing which came to my mind, like, now, I think with the… I forgot which GPT model, there is something called compute… cost as well, coming up for every operation.
So, I don't know what they call it. They call it compute units or something.
And that'll be charged along with, like, tokens.
And that's based on, like, how long your context is, and how long it has to kind of hold that context, so that's another aspect that's definitely… I've seen coming up now.
**Liudmila Molkova** 32:34 Nice. So then we would add another metric for this, I think.
**Ankit Singhal** 32:37 Yeah, yeah, so why not? I mean, usage.infoTokkens, I think, to me, sometimes, like, it kind of makes sense, like, usage.
compute units, right? So, that also kind of makes… Feels like what.
**Trask Stalnaker (Microsoft Corporation)** 32:51 So as long as… as long as the compute units that they give back is for the whole inference operation.
**Ankit Singhal** 32:59 Then…
**Trask Stalnaker (Microsoft Corporation)** 33:00 We don't have problems, and we don't need this separate counter.
Stuff, because the histograms work in that case.
the whole… Do you know if the… if that's what compute units would be, or would they break?
Thank you.
**Ankit Singhal** 33:18 Thank you.
**Trask Stalnaker (Microsoft Corporation)** 33:19 Units up for a single operation, the way they do tokens.
**Ankit Singhal** 33:23 Let me check if I can find more documentation of that.
**Trask Stalnaker (Microsoft Corporation)** 33:40 So, while Ankit's looking Surya Cash tokens are… we have, counters. It's in the… I'm kind of abbreviating here, But there is a… there are individual… Counters for the cash tokens.
But there's not a histogram.
for them.
At this point.
**Liudmila Molkova** 34:08 Yeah, we are over time. I'm thinking, I… We'll summarize the discussion on the PR.
I'll probably try to implement the usage input tokens and operation input tokens.
I think the… if there are no strong objections, I'm happy to go with it.
Alright.
I will ping Alex and ask what he thinks.
**Trask Stalnaker (Microsoft Corporation)** 34:37 Sounds good.
**Neil Yashinsky he / him** 34:38 I, I kind of… I vote for what you described, Liudmila. Seems like the right next step for what we have. Thanks. Thanks so much, everyone.
**Liudmila Molkova** 34:45 Awesome, thank you. See you on Wednesday.
**Trask Stalnaker (Microsoft Corporation)** 34:47 See ya.
